import os

from flask import Flask
from flask.ext.restless.manager import APIManager
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, Text

app = Flask(__name__, static_url_path='')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pin.db'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)


class Pin(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(Text, unique=False)
    image = Column(Text, unique=False)

db.create_all()

api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(Pin, methods=['GET', 'POST', 'DELETE', 'PUT'])

@app.route('/')
def index():
    return app.send_static_file("index.html")

app.debug = True

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)