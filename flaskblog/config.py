import os

class Config:
  ## set secret key
  ## use python: $ secrets.token_hex() to generate
  SECRET_KEY = '7532f6e85de5608e4051662da59e14005bb5f6f6274f87554dea9f523545ef65'

  ## sqlite db
  SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

  ## auto-email
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get('EMAIL_USER')
  MAIL_PASSWORD = os.environ.get('EMAIL_PASS')