from itsdangerous import URLSafeTimedSerializer

from .. import app

from flask_mail import Message, Mail


ts = URLSafeTimedSerializer(app.config["SECRET_KEY"])

def send_self_email(subject, name, email, body):
    mail = Mail()
    mail.init_app(app)
    msg = Message(subject, sender='lukecodes@gmail.com', recipients=['luke@lyft.com'])
    msg.body = "From: {} ({}) \n {}".format(name, email, body)
    mail.send(msg)

def send_email(subject, name, email, body):
    mail = Mail()
    mail.init_app(app)
    msg = Message(subject, sender='lukecodes@gmail.com', recipients=[email])
    msg.body = body
    mail.send(msg)