import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key-yep'
    SQLALCHEMY_DATABASE_URI = 'postgresql://usr:pass@localhost:5432/sqlalchemy'
    SQLALCHEMY_TRACK_MODIFICATIONS = False