from flask import Flask
# used for sqlite
from flask_sqlalchemy import SQLAlchemy
# used for user authentication
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config



## sqlite
## run in python to create table: $ from flaskblog import db
##                                $ db.create_all()
## run in python to add entry: $ from flaskblog import User
##                             $ user = User(xxx)
##                             $ db.session.add(user); db.session.commit()
##                             $ User.query.all()
## run in python to delete all: $ db.drop_all()
##                              $ db.create_all()
db = SQLAlchemy()

## for user authentication
bcrypt = Bcrypt()

## login manager used in models.py
login_manager = LoginManager()
## redirect back to login page if user access some pages before login
login_manager.login_view = 'users.login'
## bootsrap class = info
login_manager.login_message_category = 'info'

## auto-email
mail = Mail()


def create_app(config_class=Config):
  app = Flask(__name__)
  ## import config from Config class
  app.config.from_object(Config)

  ## init extensions with app
  db.init_app(app)
  bcrypt.init_app(app)
  login_manager.init_app(app)
  mail.init_app(app)

  ## import here to deal with circular import issue
  ## use Blueprint to import routes
  from flaskblog.users.routes import users
  from flaskblog.posts.routes import posts
  from flaskblog.main.routes import main
  from flaskblog.errors.handlers import errors
  app.register_blueprint(users)
  app.register_blueprint(posts)
  app.register_blueprint(main)
  app.register_blueprint(errors)

  return app
