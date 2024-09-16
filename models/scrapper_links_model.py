from . import db

class ScrapperLinks(db.Model):
    __tablename__ = 'scrapper_links'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    domen_id = db.Column(db.Integer, db.ForeignKey('domens.id'), nullable=False)
    link = db.Column(db.String, nullable=False, unique=True)
    handle = db.Column(db.Boolean, nullable=False, default=False)
    title = db.Column(db.String, default='Parse error')
    html_content = db.Column(db.String)
    search_request = db.Column(db.String)
    
    # Relationships
    post = db.relationship('Posts', back_populates='scrapper_link')
    domen = db.relationship('Domens', back_populates='scrapper_links')

    def to_dict(self):
        return {
            'id': self.id,
            'link': self.link,
            'handle': self.handle,
            'domen': self.domen.domen if self.domen else None,
            'title': self.title,
            'html_content': self.html_content,
            'search_request': self.search_request
        }
