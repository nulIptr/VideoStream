"""
The flask application package.
"""

from flask import Flask



#from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from bs4 import BeautifulSoup

bootstrap=Bootstrap()
#db=SQLAlchemy()

def create_app():
    app = Flask(__name__)
    bootstrap.init_app(app)
    
    #db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app