# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
from celery.schedules import crontab

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    SECRET_KEY = (
        os.environ.get('SECRET_KEY') or
        '\x11\xbe\xbb\xf0\x7fz\x9d\x01\x07\xa0'
        '\xd0J\xec\xbbw\nfc\xc5Q\xd0\x6cd\xf1')
    CSRF_ENABLED = True

    SQLALCHEMY_RECORD_QUERIES = True
    # SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get('DEV_DATABASE_URL')
        or 'postgresql+psycopg2://stepbystep:ssss@localhost/stepbystep')

    # redis
    REDIS_URL = 'redis://%s:%s/%s' % (
        os.environ.get('REDIS_HOST', 'localhost'),
        os.environ.get('REDIS_PORT', '6379'),
        os.environ.get('REDIS_DATABASE', '1'),
    )

    # celery
    CELERY_BROKER_URL = 'redis://%s:%s' % (
        os.environ.get('REDIS_HOST', 'localhost'),
        os.environ.get('REDIS_PORT', '6379'))

    CELERYBEAT_SCHEDULE = {
        'test': {
            'task': 'stepbystep.core.tasks.test',
            'schedule': crontab(minute='*/1'),
            'args': (1, 2, 3)
        },
    }

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
