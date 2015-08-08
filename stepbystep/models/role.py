# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from sqlalchemy import sql

from stepbystep import db


__all__ = [
    'RoleModel',
    'Permission',
]


class Permission(object):
    ADMINISTER = 0x80


class RoleModel(db.Model):

    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    default = db.Column(
        db.Boolean, default=False, index=True, server_default=sql.false())
    permissions = db.Column(db.Integer)
    date_created = db.Column(
        db.DateTime, nullable=False,
        server_default=db.func.current_timestamp())

    @staticmethod
    def insert_roles():
        roles = {
            'User': (0x10, True),
            'Administrator': (0xff, False),
        }
        for r in roles:
            role = RoleModel.query.filter_by(name=r).first()
            if role is None:
                role = RoleModel(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()

    def __repr__(self):
        return 'Role: %r' % self.name
