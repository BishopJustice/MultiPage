from app import db

from werkzeug import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    pwdhash = db.Column(db.String(100))
    joined = db.Column(db.String(200))
   
    def __init__(self, firstname, lastname, email, password, joined):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.email = email.lower()
        self.set_password(password)
        self.joined = joined
     
    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)
   
    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)

class Project(db.Model):
    __tablename__ = 'projects'
    pid = db.Column(db.Integer, primary_key = True)
    uid = db.Column(db.Integer, db.ForeignKey('users.uid'))
    name = db.Column(db.String(50))
    items = db.relationship("Item")
    links = db.relationship("Link")


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key = True)
    pid = db.Column(db.Integer, db.ForeignKey('projects.pid'))
    description = db.Column(db.String(500), nullable = False)
    label = db.Column(db.String(50))
    priority = db.Column(db.String(50))
    state = db.Column(db.String(10), nullable = False)
    opened_at = db.Column(db.String(200), nullable = False)
    resolved_at = db.Column(db.String(200))
    uid = db.Column(db.Integer, db.ForeignKey('users.uid'))


class Link(db.Model):
    __tablename__ = 'links'
    id = db.Column(db.Integer, primary_key = True)
    pid = db.Column(db.Integer, db.ForeignKey('projects.pid'))
    url = db.Column(db.String(600))
    link_name= db.Column(db.String(50))
    






