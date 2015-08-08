# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from stepbystep import db


__all__ = [
    'SolutionModel',
]


class SolutionModel(db.Model):

    __tablename__ = 'solution'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False, index=True)
    # 对应 ProblemModel.id，而不是ProblemModel.problem_id
    problem_id = db.Column(db.Integer, nullable=False, index=True)
    language = db.Column(db.String(64))
    date_submit = db.Column(
        db.DateTime, nullable=False, index=True,
        server_default=db.func.current_timestamp())
    date_created = db.Column(
        db.DateTime, nullable=False, index=True,
        server_default=db.func.current_timestamp())

    def __repr__(self):
        return 'Solution: %r' % self.id
