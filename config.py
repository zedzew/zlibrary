import os

class BaseConfig(object):
    basedir = os.path.abspath(os.path.dirname(__file__))
    DATABASE = os.path.join(basedir, 'app.db')
    CSRF_ENABLED = True
    SECRET_KEY = 'P\xa1<\t\x13\xbe\xbfI\xeb\x1c#1\x9b\xe2\xfcP'
    WHOOSH_BASE = os.path.join(basedir, 'search.db')  
    MAX_SEARCH_RESULTS = 50 

class ProductionConfig(BaseConfig):
    DEBUG = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True

#class TestingConfig(BaseConfig):
  #  TESTING = True

