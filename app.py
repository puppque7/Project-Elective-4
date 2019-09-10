from flask import Flask, render_template, url_for, flash, redirect,session
from form import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length
import os

PEOPLE_FOLDER = os.path.join('static','people_photo')
db = SQLAlchemy()
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/appdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

class User(db.Model):
    __tablename__ = "register"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(121), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True)

def __repr__(self):
    return "<User %r>" % self.username


@app.route("/")
def home():
    fl = os.path.join(app.config['UPLOAD_FOLDER'], 'final.gif')
    return render_template('home.html',user_image=fl)


@app.route("/register", methods=['GET', 'POST'])
def register():
    username = None
    email = None
    password = None
    cpassword = None

    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        login = User(username=username,email=email,password=password)

        db.session.add(login)
        db.session.commit()

        return f'<h1>{form.username.data}, you have been registered successfully! Click <a href="/login">here</a> to login.</h1>', 'success'
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if user.password==form.password.data:
                return f'<CENTER>Welcome,{form.username.data}!</CENTER> '
            else:
                return "<h1><center>INVALID!</center></h1>"
        else:
            return "<h1><center>INVALID!</center></h1>"
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
