import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

from models import db
from sqlalchemy.exc import IntegrityError
from models.posts_model import Posts
from models.domens_model import Domens
from services.domens_service import createDomen, getDomen

def getPosts():
    try:
        records = db.session.query(Posts).all()

        if records:
            print(f"========== getPosts: Posts found: {records}")
            return records
        else: 
            print(f"========== getPosts: Posts don\'t found!")
            return None
    except IntegrityError as e:
        db.session.rollback()
        print(f"========== getPosts: An error occurred while deleting the record: {e}")
        return False
    
def createPost(link_id, title):
    record = Posts(
        link_id=link_id,
        title=title
    )

    try:
        db.session.add(record)
        db.session.commit()

        return True
    except IntegrityError as e:
        db.session.rollback()
        print(f'========== createPost: Integrity Error while create Post: {e}')

        return False
    except Exception as e:
        db.session.rollback()
        print(f'========== createPost: Error while create Post: {e}')
        
        return False

def updatePostInstructionID(post_id, instruction_id):
    try:
        record = db.session.query(Posts).filter_by(id=post_id).one_or_none()

        if record:
            record.instruction_id = instruction_id
            db.session.commit()
            return True
        else:
            print(f"========== updatePostInstructionID: Error - No record found with id={post_id}")
            return False
    except IntegrityError as e:
        db.session.rollback()
        print(f'========== updatePostInstructionID: Integrity Error: {e}')
        return False
    except Exception as e:
        db.session.rollback()
        print(f'========== updatePostInstructionID: Unexpected Error: {e}')
        return False

def updatePostTitle(post_id, new_title):
    try:
        record = db.session.query(Posts).filter_by(id=post_id).one_or_none()

        if not record:
            print(f"========== updatePostTitle: Error - No record found with id={post_id}")
            return False
    
        record.title = new_title
        db.session.commit()
        return True
    except IntegrityError as e:
        db.session.rollback()
        print(f'========== updatePostTitle: Integrity Error: {e}')
        return False
    except Exception as e:
        db.session.rollback()
        print(f'========== updatePostTitle: Unexpected Error: {e}')
        return False
