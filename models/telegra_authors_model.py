from . import db

class TelegraAuthors(db.Model):
    __tablename__ = 'telegra_authors'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    token = db.Column(db.String, nullable=False, unique=True)
    telegram_user_id = db.Column(db.Integer, nullable=True, unique=True)
    telegram_user_name = db.Column(db.String, nullable=False, unique=True)

    telegra_posts = db.relationship('TelegraPosts', back_populates='telegra_author')