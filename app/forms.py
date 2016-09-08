from flask_wtf import Form
from wtforms.fields import TextField, BooleanField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import Required, ValidationError
from wtforms import validators
from models import User
from app import db


class ContactForm(Form):
    name = TextField("Name",  [validators.Required("Please enter a name")])
    email = TextField("Email",  [validators.Required("Valid Email Required"), validators.Email()])
    subject = TextField("Subject",  [validators.Required("Pleas enter a subject")])
    message = TextAreaField("Message",  [validators.Required("Body is required")])
    submit = SubmitField("Send")

class SignupForm(Form):
    firstname = TextField("First name",  [validators.Required("Please enter your first name.")])
    lastname = TextField("Last name",  [validators.Required("Please enter your last name.")])
    email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter a valid email address.")])
    password = PasswordField('Password', [validators.Required("Please enter a password.")])
    submit = SubmitField("Create account")
 
    def __init__(self, *args, **kwargs):
      Form.__init__(self, *args, **kwargs)
 
    def validate(self):
      if not Form.validate(self):
        return False
     
      user = db.session.query(User).filter_by(email = self.email.data.lower()).first()
      if user:
        self.email.errors.append("That email is already taken")
        return False
      else:
        return True

class SigninForm(Form):
  email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
  password = PasswordField('Password', [validators.Required("Please enter a password.")])
  submit = SubmitField("Sign In")
   
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
 
  def validate(self):
      if not Form.validate(self):
        return False
     
      user = db.session.query(User).filter_by(email = self.email.data.lower()).first()
      if user and user.check_password(self.password.data):
        return True
      else:
        self.email.errors.append("Invalid e-mail or password")
        return False