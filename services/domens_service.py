import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

from models import db
from sqlalchemy.exc import IntegrityError
from models.domens_model import Domens

def createDomen(domen):
    try:
        record = Domens(domen=domen)
        db.session.add(record)
        db.session.commit()
        return record
    except IntegrityError as e:
        db.session.rollback()
        print(f"Record already exists! {e}")
        
        existing_record = db.session.query(Domens).filter_by(domen=domen).first()
        
        if existing_record:
            return existing_record.id
        else:
            return None

def deleteDomen(domen):
    try:
        record = db.session.query(Domens).filter_by(domen=domen).first()
        
        if record:
            db.session.delete(record)
            db.session.commit()
            print(f"Record with domen '{domen}' has been deleted.")
            return True
        else:
            print(f"No record found with domen '{domen}'.")
            return False
    except IntegrityError as e:
        db.session.rollback() 
        print(f"An error occurred while deleting the record: {e}")
        return False
    
def updateDomen(old_domen, new_domen):
    try:
        # Поиск записи по значению old_domen
        record = db.session.query(Domens).filter_by(domen=old_domen).first()
        
        if record:
            record.domen = new_domen  # Изменение значения domen
            db.session.commit()
            print(f"Record updated from '{old_domen}' to '{new_domen}'.")
            return record.id
        else:
            print(f"No record found with domen '{old_domen}'.")
            return None
    except IntegrityError as e:
        db.session.rollback()
        print(f"An error occurred while updating the record: {e}")
        return None
    
def getDomen(domen):
    try:
        record = db.session.query(Domens).filter_by(domen=domen).first()
        
        if record:
            print(f"Record successfully found {domen}.")
            return record
        else:
            print(f"No record found with domen '{domen}'.")
            return None
    except IntegrityError as e:
        db.session.rollback()
        print(f"An error occurred while getting the record: {e}")
        return None