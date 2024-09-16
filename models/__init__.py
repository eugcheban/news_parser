from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .domens_model import Domens
from .scrapper_links_model import ScrapperLinks
from .posts_model import Posts
from .instructions_model import Instructions
from .telegra_authors_model import TelegraAuthors
from .telegra_posts_languages_model import TelegraPostsLanguages
from .telegra_posts_model import TelegraPosts
