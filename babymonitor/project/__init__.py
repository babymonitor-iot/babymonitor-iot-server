from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate


app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from .model import db_model
from .controllers import main_controller

db.create_all()
