import os

base_dir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'gis-2016'
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = 'gis-2016'
    LOG_FILENAME = '/var/www/gis_boilerplate/logs/app.log'
    STATIC_FOLDER = '/var/www/gis_boilerplate/client/static'
    TEMPLATES_FOLDER = '/var/www/gis_boilerplate/client/templates'
    TMP_DIR = '/var/www/gis_boilerplate/tmp'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://gisuser:youcantguess@localhost:5432/gis_demo'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    pass


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)