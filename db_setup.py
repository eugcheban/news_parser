def create_db_structure(app, db):
    try:
        with app.app_context():
            from models.scrapper_links_model import ScrapperLinks
            from models.posts_model import Posts
            from models.domens_model import Domens
            from models.telegra_posts_model import TelegraPosts
            from models.instructions_model import Instructions
            from models.telegra_posts_languages_model import TelegraPostsLanguages
            from models.telegra_authors_model import TelegraAuthors

            db.create_all()
            print("All tables created successfully from db_setup().")
    except Exception as e:
        print(f"An error occurred while creating tables from db_setup(): {e}")

def delete_db_structure(app, db):
    try:
        with app.app_context():
            db.drop_all()
            print("All tables successfully deleted from db.drop_all().")
    except Exception as e:
        print(f"An error occurred while deleting the tables from db.drop_all(): {e}")