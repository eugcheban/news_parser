from . import db

class Instructions(db.Model):
    __tablename__ = 'instructions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    instruction = db.Column(db.String, nullable=False)

    post = db.relationship('Posts', back_populates='instructions')