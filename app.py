import os, requests
from config import Config, TestingConfig, DevelopmentConfig, ProductionConfig
from utils import get_domain

from flask import Flask, render_template, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
from telegraph import Telegraph
from db_setup import create_db_structure, delete_db_structure
from dotenv import load_dotenv
from models import db, seed
import logging
from sqlalchemy import event

from services.domens_service import createDomen, deleteDomen, updateDomen
from services.scrapper_links_service import createScrapperLink, deleteScrapperLink, getScrapperLinks, get_numScrapperLinks, get_num_unhandledScrapperLinks, setHandle
from services.posts_service import getPosts, createPost, updatePostInstructionID, updatePostTitle
from services.instructions_service import updateInstruction, createInstruction
from sel import Driver
from soup import Soup
from dolp import Dolphin

app = Flask(__name__)

load_dotenv()
env = os.environ.get('FLASK_ENV', 'testing')

if env == 'development':
    app.config.from_object(DevelopmentConfig)
elif env == 'testing':
    app.config.from_object(TestingConfig)
elif env == 'production':
    app.config.from_object(ProductionConfig)
else:
    app.config.from_object(Config)

db.init_app(app)

# Включение логгирования SQLAlchemy
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

def before_create(target, connection, **kw):
    print(f"Creating table: {target.name}")

def after_create(target, connection, **kw):
    print(f"Table created: {target.name}")

# Привязка событий к моделям
for table in db.metadata.tables.values():
    event.listen(table, 'before_create', before_create)
    event.listen(table, 'after_create', after_create)



#======      API
#=============================================================
@app.route('/api/links')
def api_links():
    records = getScrapperLinks()
    return jsonify([record.to_dict() for record in records])

@app.route('/api/posts') # => Routes using: scrapper.js
def api_posts():
    records = getPosts()
    return jsonify([record.to_dict() for record in records])

@app.route('/update-instruction', methods=['POST'])
def update_instruction():
    data = request.json
    
    post_id = data.get('post_id')
    instruction_id = data.get('instruction_id')
    instruction = data.get('instruction')
    
    if instruction_id:
        updateInstruction(id=instruction_id, instruction=instruction)
    else:
        instruction_id = createInstruction(instruction=instruction)

    updatePostInstructionID(post_id=post_id, instruction_id=instruction_id)

    return jsonify({'type': 'success', 'message': 'Server: Instruction has been updated!'})

@app.route('/scrapper-request', methods=['POST'])
def scrapper_request():
    data = request.json

    search_request = data.get('search_request')
    num = data.get('num')

    driver = Driver()

    try:
        google_result = driver.goToPage(f'https://www.google.com/search?q={search_request}&tbm=nws&hl=en&num={num}&tbs=qdr:d')
    except Exception as e:
        return jsonify({'type': 'error', 'message': str(e)})
    
    soup_t = Soup(google_result)
    links = soup_t.parseLinks()
    
    for link in links:
        html_content = driver.goToPage(link['link'])

        soup_t = Soup(html_content)
        title = soup_t.get_title()
        print(f"===================================== {title}")

        createScrapperLink(
            domen=get_domain(link['link']),
            link=link['link'],
            title=title,
            html_content=html_content,
            search_request=search_request
        )
        
    driver.close_driver()
    return jsonify({'type': 'success', 'message': 'Request has been proceed!'})

@app.route('/scrapper-transfer', methods=['POST'])
def scrapper_transfer(): # => Routes using: scrapper.js
    data = request.json

    if len(data['links']) > 0:
        for link in data['links']:
            if not createPost(
                link_id=link.get('id'),
                title=link.get('title')
            ): 
                return jsonify({'type': 'error', 'message': 'Error creating post!'})
                
            if not setHandle(
                scrapperlink_id=link.get('id'),
                handle=True
            ):
                return jsonify({'type': 'error', 'message': 'Error setting handle!'})
                

        return jsonify({'type': 'success', 'message': 'Links were transfered'})

@app.route('/parser-update-title', methods=['POST'])
def parser_update_row():
    data = request.json

    if not data:
        return jsonify({'type':'error', 'message':'Error while getting request data!'})

    if not updatePostTitle(
            post_id=data['post_id'],
            new_title=data['title'],
        ):
        return jsonify({'type':'error', 'message':'Error while updating title!'})

    return jsonify({'type':'success', 'message':'The tittle has been updated!'})






#=============================================================

#======      Routes
#=============================================================
@app.route('/')
def template_index():
    links_unhandle = get_num_unhandledScrapperLinks()
    links_total = get_numScrapperLinks()

    return render_template('index.html', links_unhandle=links_unhandle, links_total=links_total)

@app.route('/scrapper')
def template_scrapper():
    links = getScrapperLinks()

    return render_template('scrapper.html', links=links)

@app.route('/example')
def example():

    return render_template('link_example.html')

@app.route('/parser')
def parser():

    return render_template('parser.html')

@app.route('/news-editor', methods=['POST', 'GET'])
def news_editor():
    if request.method == 'POST':
        title = request.json.get('title')
        author = request.json.get('author')
        content = request.json.get('content')
        telegra = Telegraph()
        response = telegra.create_page(title, author, content)
        url = response['result']['url']
        print(response)
        return jsonify({'status': 'success', 'url': url})
    return render_template('news-editor.html')


@app.route('/proxy')
def proxy():
    url = request.args.get('url')
    response = requests.get(url)
    return Response(response.content, content_type=response.headers['content-type'])
#=============================================================

if __name__ == '__main__':
    #before using app, should be create db structure
    #seed_data() - for development

    #delete_db_structure(app, db)
    #create_db_structure(app, db) 
    with app.app_context():
        #seed.seed_data()
        pass
    
    app.run()
