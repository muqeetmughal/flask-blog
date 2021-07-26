import os
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

APP_VERSION = 'v1.000.0'

SECRET_KEY = os.environ.get('SECRET_KEY')

# DATABASE_URI = 'sqlite:///database.db'
DATABASE_URI = 'mysql+pymysql://root:@localhost/flask_blog'
DEBUG_MODE = True

SERVER_PORT = 8000
SERVER_ADDRESS = '127.0.0.1'
API_VERSION = 'v1'
