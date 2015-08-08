# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from stepbystep import db


__all__ = [
    'ProblemModel',
]


class ProblemModel(db.Model):

    __tablename__ = 'problem'

    id = db.Column(db.Integer, primary_key=True)
    oj_name = db.Column(db.String(64), nullable=False)
    problem_id = db.Column(db.String(64), nullable=False)
    category_id = db.Column(db.Integer)
    ordinal = db.Column(db.Integer)
    date_created = db.Column(
        db.DateTime, nullable=False, index=True,
        server_default=db.func.current_timestamp())

    def __repr__(self):
        return '%r: %r' % (self.oj_name, self.problem_id)
