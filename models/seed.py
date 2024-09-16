from . import db
from models.scrapper_links_model import ScrapperLinks
from models.posts_model import Posts
from models.domens_model import Domens
from models.telegra_posts_model import TelegraPosts
from models.instructions_model import Instructions
from models.telegra_posts_languages_model import TelegraPostsLanguages
from models.telegra_authors_model import TelegraAuthors

def seed_data():
    telegra_author1 = TelegraAuthors(name='EagleNet', token='FJKSHF3298F298F', telegram_user_id=484894, telegram_user_name='@eaglenet_support')
    telegra_author2 = TelegraAuthors(name='EagleNetRu', token='FFKSHF3298F298F', telegram_user_id=484823, telegram_user_name='@eaglenet_support_ru')

    db.session.add(telegra_author1)
    db.session.add(telegra_author2)
    db.session.commit()

    telegra_posts_languages1 = TelegraPostsLanguages(language='EN')
    telegra_posts_languages2 = TelegraPostsLanguages(language='RU')

    db.session.add(telegra_posts_languages1)
    db.session.add(telegra_posts_languages2)
    db.session.commit()

    instruction1 = Instructions(instruction="""
iframeContent.find('.news-content p').each(function() {
    content.push(processElement(this));
}); 
""")
    instruction2 = Instructions(instruction="""
iframeContent.find('.news-content p').each(function() {
    content.push(processElement(this));
    content.push(processElement(this));
    content.push(processElement(this));
}); 
""")
    
    db.session.add(instruction1)
    db.session.add(instruction2)
    db.session.commit()

    tg_post1 = TelegraPosts(author_id=1, language_id=1, title='title - tg_post1', content='content - tg_post1', link='https://telegra.ph/tg_post1')
    tg_post2 = TelegraPosts(author_id=1, language_id=2, title='title - tg_post2', content='content - tg_post2', link='https://telegra.ph/tg_post2')

    db.session.add(tg_post1)
    db.session.add(tg_post2)
    db.session.commit()


    domen1 = Domens(domen='db.com')

    db.session.add(domen1)
    db.session.commit()

    # Create a scrapper_links
    link1 = ScrapperLinks(domen_id=1, link='https://www.db.com/news/detail/20240724-deutsche-bank-reports-on-the-second-quarter-of-2024')
    link2 = ScrapperLinks(domen_id=1, link='https://flow.db.com/more/esg/biodiversity-funding-our-future#!')
    
    db.session.add(link1)
    db.session.add(link2)
    db.session.commit()
    
    post1 = Posts(link_id=1, instruction_id=1, telegra_post_id=1, title='Posts example 1')
    post2 = Posts(link_id=2, instruction_id=2, telegra_post_id=2, title='Posts example 2')
    
    db.session.add(post1)
    db.session.add(post2)
    db.session.commit()



    

    



    

    

    print('Database seeded!')

if __name__ == '__main__':
    seed_data()