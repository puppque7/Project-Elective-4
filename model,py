from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.model):
    __tablename__ = "register"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(121), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True)



def __repr__(self):
    return "<User %r>" % self.username
