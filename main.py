import os
from flask import Flask
from flask_restful import Api
from settings import SERVER_ADDRESS, SERVER_PORT, DEBUG_MODE, DATABASE_URI, SECRET_KEY
from settings import db, ma
from models.all_models import *
from routes import urls

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_pyfile('settings.py')
app.config.update(SECRET_KEY=SECRET_KEY)

api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


urls(api)

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    app.run(port=SERVER_PORT, host=SERVER_ADDRESS, debug=DEBUG_MODE)
