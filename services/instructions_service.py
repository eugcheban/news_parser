import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

from models import db
from sqlalchemy.exc import IntegrityError
from models.instructions_model import Instructions

def updateInstruction(id, instruction):
    try:
        record = db.session.query(Instructions).filter_by(id=id).first()

        if record:
            print(f"updateInstruction: Record to update found: {record}")
            record.instruction = instruction
            db.session.commit()

            return True
        else: 
            print(f"updateInstruction: Record doesn\'t found!")
            return None
    
    except IntegrityError as e:
        db.session.rollback()
        print(f"updateInstruction: An error occurred while updating the record: {e}")
        
        return False
    except Exception as e:
        db.session.rollback()
        print(f"updateInstruction: An unexpected error occurred: {e}")
        
        return False
    
def createInstruction(instruction):
    record = Instructions(
        instruction=instruction
    )

    try:
        db.session.add(record)
        db.session.commit()

        return record.id
    except IntegrityError as e:
        db.session.rollback()
        print(f"createInstruction: An error occurred while creating the record: {e}")
        
        return False
    except Exception as e:
        db.session.rollback()
        print(f"createInstruction: An unexpected error occurred: {e}")
        
        return False