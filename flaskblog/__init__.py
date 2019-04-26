from flask import Flask
# used for sqlite
from flask_sqlalchemy import SQLAlchemy
# used for user authentication
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
## set secret key
## use python: $ secrets.token_hex() to generate
app.config['SECRET_KEY'] = '7532f6e85de5608e4051662da59e14005bb5f6f6274f87554dea9f523545ef65'
## sqlite
## run in python to create table: $ from flaskblog import db
##                                $ db.create_all()
## run in python to add entry: $ from flaskblog import User
##                             $ user = User(xxx)
##                             $ db.session.add(user); db.session.commit()
##                             $ User.query.all()
## run in python to delete all: $ db.drop_all()
##                              $ db.create_all()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

## for user authentication
bcrypt = Bcrypt(app)

## login manager used in models.py
login_manager = LoginManager(app)
## redirect back to login page if user access some pages before login
login_manager.login_view = 'login'
## bootsrap class = info
login_manager.login_message_category = 'info'

## import here to deal with circular import issue
from flaskblog import routes