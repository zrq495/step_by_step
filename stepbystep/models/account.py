# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from stepbystep import db


__all__ = [
    'OJAccountModel',
]


class OJAccountModel(db.Model):

    __tablename__ = 'oj_account'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    oj_name = db.Column(db.String(64), index=True, nullable=False)
    username = db.Column(db.String(256), nullable=False)
    nickname = db.Column(db.String(256))
    accept = db.Column(db.Integer, default=0, server_default='0')
    submit = db.Column(db.Integer, default=0, server_default='0')
    rating = db.Column(db.Integer, default=0, server_default='0')
    date_created = db.Column(
        db.DateTime, nullable=False, index=True,
        server_default=db.func.current_timestamp())

    def __repr__(self):
        return '%r: %r' % (self.oj_name, self.username)
