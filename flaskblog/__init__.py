from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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

## import here to deal with circular import issue
from flaskblog import routes