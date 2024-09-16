from . import db

class Domens(db.Model):
    __tablename__ = 'domens'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    domen = db.Column(db.String, nullable=False, unique=True)

    scrapper_links = db.relationship('ScrapperLinks', back_populates='domen')
