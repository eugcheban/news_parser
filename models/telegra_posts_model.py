from . import db

class TelegraPosts(db.Model):
    __tablename__ = 'telegra_posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_id = db.Column(db.Integer, db.ForeignKey('telegra_authors.id'), nullable=False)
    language_id = db.Column(db.Integer, db.ForeignKey('telegra_posts_languages.id'), nullable=False)
    title = db.Column(db.String, nullable=False, unique=True)
    content = db.Column(db.String, nullable=False)
    link = db.Column(db.String, nullable=False, unique=True)
    
    post = db.relationship('Posts', back_populates='telegra_posts')
    telegra_author = db.relationship('TelegraAuthors', back_populates='telegra_posts')
    telegra_posts_languages = db.relationship('TelegraPostsLanguages', back_populates='telegra_posts')