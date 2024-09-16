from . import db

class TelegraPostsLanguages(db.Model):
    __tablename__ = 'telegra_posts_languages'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    language = db.Column(db.String, nullable=False, unique=True)
    
    telegra_posts = db.relationship('TelegraPosts', back_populates='telegra_posts_languages')