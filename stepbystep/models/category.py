# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from stepbystep import db


__all__ = [
    'CategoryModel',
]


class CategoryModel(db.Model):

    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    url = db.Column(db.String(64))
    parent_id = db.Column(db.Integer)
    date_created = db.Column(
        db.DateTime, nullable=False, index=True,
        server_default=db.func.current_timestamp())

    parent = db.relationship(
        'CategoryModel',
        backref=db.backref('children', lazy='dynamic'),
        remote_side='[CategoryModel.id]',
        primaryjoin='CategoryModel.id==CategoryModel.parent_id',
        foreign_keys='[CategoryModel.parent_id]')

    problems = db.relationship(
        'ProblemModel',
        primaryjoin='CategoryModel.id==ProblemModel.category_id',
        foreign_keys='[ProblemModel.category_id]',
        backref=db.backref('category', lazy=True),
        lazy='dynamic',
        uselist=True)

    @property
    def full_name(self):
        name = [self.name]
        parent = self.parent
        while parent:
            name.append(parent.name)
            parent = parent.parent
        return ': '.join(name[::-1])

    def __repr__(self):
        return self.full_name
