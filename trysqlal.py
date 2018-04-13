from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'DB URL HERE'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
        
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(140), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    author = db.relationship('User',
        backref=db.backref('messages', lazy=True))

    def __repr__(self):
        return '<Message %r>' % self.content
        
