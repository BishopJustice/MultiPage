from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


app = Flask(__name__)

app.config.from_object('config')
engine = create_engine('mysql://root@localhost/multipage')
Session = sessionmaker(bind=engine)
db = SQLAlchemy(app)

from app import views, models
