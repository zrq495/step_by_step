# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from celery import Celery

from stepbystep import app
from crawl import (
    AccountCrawler
)


def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

celery = make_celery(app)


@celery.task()
def account_crawler(origin_oj, username):
    crawler = AccountCrawler()
    crawler.crawl(
        origin_oj,
        username,
    )


@celery.task()
def test(args, **kwargs):
    print args, kwargs
