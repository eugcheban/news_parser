import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

from models import db
from sqlalchemy.exc import IntegrityError
from models.scrapper_links_model import ScrapperLinks
from models.domens_model import Domens
from services.domens_service import createDomen, getDomen

def createScrapperLink(domen, link, title, html_content, search_request):
    existing_record = db.session.query(ScrapperLinks).filter_by(link=link).first()

    if existing_record:
        print(f"createScrapperLink: Duplicate record found! {existing_record.id}")
        return None
    
    record_domen = None
    try:
        record_domen = getDomen(domen)
        if not record_domen:
            record_domen = createDomen(domen)
    except Exception as e:
        print(f"createScrapperLink: Error occured while creating \ getting domen in createScrappedLink function: {e}")
        return None
    
    try:
        record = ScrapperLinks(
            domen_id=record_domen.id, 
            link=link,
            title=title,
            html_content=html_content,
            search_request=search_request
        )
        db.session.add(record)
        db.session.commit()
        return record
    except IntegrityError as e:
        db.session.rollback()
        print(f"createScrapperLink: Record already exists! {e}")
        return None

def deleteScrapperLink(id):
    try:
        record = db.session.query(ScrapperLinks).filter_by(id=id).first()
        
        if record:
            db.session.delete(record)
            db.session.commit()
            print(f"Record with domen '{id}' has been deleted.")
            return True
        else:
            print(f"No record found with link {id}.")
            return False
    except IntegrityError as e:
        db.session.rollback() 
        print(f"deleteScrapperLink: An error occurred while deleting the record: {e}")
        return False
    
def getScrapperLinks():
    try:
        records = db.session.query(ScrapperLinks).all()
        
        if records:
            print(f"getScrapperLinks: Records found!")
            return records
        else:
            print(f"getScrapperLinks: No records found.")
            return None
    except IntegrityError as e:
        db.session.rollback()
        print(f"getScrapperLinks: An error occurred while getting links: {e}")
        return None

def getScrapperLinkById(id):
    try:
        record = db.session.query(ScrapperLinks).filter_by(id=id).first()
        
        if record:
            print(f"getScrapperLinkById: Record by id found!")
            return record
        else:
            print(f"getScrapperLinkById: No records by id found.")
            return None
    except IntegrityError as e:
        db.session.rollback()
        print(f"getScrapperLinkById: An error occurred while getting links: {e}")
        return None
    
def get_num_unhandledScrapperLinks():
    try:
        records = db.session.query(ScrapperLinks).filter_by(handle=False).all()

        if records:
            print(f"Unandled records found!")
            return len(records)
    except Exception as e:
        print(f"get_num_unhandledScrapperLinks: An error occurred while getting links: {e}")
        return None

def get_numScrapperLinks():
    try:
        records = db.session.query(ScrapperLinks).all()

        if records:
            print(f"Links records found!")
            return len(records)
    except Exception as e:
        print(f"get_numScrapperLinks: An error occurred while getting links: {e}")
        return None
    
def setHandle(scrapperlink_id, handle:bool = False):
    record = db.session.query(ScrapperLinks).filter_by(id=scrapperlink_id).one_or_none()

    try:
        if record:
            record.handle = handle
            db.session.commit()
        else:
            print(f"========== setHandle: Error - No record found with id={scrapperlink_id}")
            
            return False
        
        return True
    except IntegrityError as e:
        db.session.rollback()
        print(f'========== setHandle: Integrity Error: {e}')
        
        return False
    except Exception as e:
        db.session.rollback()
        print(f'========== setHandle: Unexpected Error: {e}')
        
        return False
