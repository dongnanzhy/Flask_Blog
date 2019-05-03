from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User


class RegistrationForm(FlaskForm):
  # with form validation
  username = StringField('Username',
                          validators=[DataRequired(), Length(min=2, max=20)])
  email = StringField('Email', 
                      validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  confirm_password = PasswordField('Confirm Password', 
                                    validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Sign Up')

  ## Customized validation of form
  def validate_username(self, username):
    ## check whether input username already in database
    user = User.query.filter_by(username=username.data).first()
    if user:
      raise ValidationError('That username is taken. Please choose a different one.')

  def validate_email(self, email):
    ## check whether input email already in database
    user = User.query.filter_by(email=email.data).first()
    if user:
      raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
  # with form validation
  email = StringField('Email', 
                      validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  remember = BooleanField('Remember Me')
  submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
  # with form validation
  username = StringField('Username',
                          validators=[DataRequired(), Length(min=2, max=20)])
  email = StringField('Email', 
                      validators=[DataRequired(), Email()])
  submit = SubmitField('Update')
  picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])

  ## Customized validation of form
  def validate_username(self, username):
    ## check whether input username already in database, 
    ## only if username not equals to previous username
    if username.data != current_user.username:
      user = User.query.filter_by(username=username.data).first()
      if user:
        raise ValidationError('That username is taken. Please choose a different one.')

  def validate_email(self, email):
    ## check whether input email already in database, 
    ## only if email not equals to previous email
    if email.data != current_user.email:
      user = User.query.filter_by(email=email.data).first()
      if user:
        raise ValidationError('That email is taken. Please choose a different one.')

class RequestResetForm(FlaskForm):
  email = StringField('Email', 
                      validators=[DataRequired(), Email()])
  submit = SubmitField('Request Password Reset')

  def validate_email(self, email):
    user = User.query.filter_by(email=email.data).first()
    if user is None:
      raise ValidationError('There is no account with that email. You must register first.')

class ResetPasswordForm(FlaskForm):
  password = PasswordField('Password', validators=[DataRequired()])
  confirm_password = PasswordField('Confirm Password', 
                                    validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Reset Password')