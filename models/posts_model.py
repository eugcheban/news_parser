from . import db

class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    link_id = db.Column(db.Integer, db.ForeignKey('scrapper_links.id'))
    instruction_id = db.Column(db.Integer, db.ForeignKey('instructions.id'))
    telegra_post_id = db.Column(db.Integer, db.ForeignKey('telegra_posts.id'))
    title = db.Column(db.String, nullable=False)

    scrapper_link = db.relationship('ScrapperLinks', back_populates='post')
    instructions = db.relationship('Instructions', back_populates='post')
    telegra_posts = db.relationship('TelegraPosts', back_populates='post')

    def to_dict(self):
        return {
            'post_id': self.id,
            'domen': self.scrapper_link.domen.domen if self.scrapper_link and self.scrapper_link.domen else None,
            'link': self.scrapper_link.link if self.scrapper_link.link else None,
            'title': self.title if self.title else None,
            'instruction': self.instructions.instruction if self.instructions else None,
            'instruction_id': self.instructions.id if self.instructions else None,
            'telegra_post': self.telegra_posts.link if self.telegra_posts else False,
            'html_content': self.scrapper_link.html_content if self.scrapper_link else None
        }