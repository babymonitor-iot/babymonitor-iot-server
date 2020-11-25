from flask import Flask
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)
db = SQLAlchemy(app)

db.create_all()

from .model import db_model
from .controllers import main_controller
