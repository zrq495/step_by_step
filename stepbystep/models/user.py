# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from flask.ext.login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import sql

from stepbystep import db, login_manager
from .role import Permission


__all__ = [
    'UserModel',
]


@login_manager.user_loader
def load_user(user_id):
    return UserModel.query.get(int(user_id))


class UserModel(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(
        db.String(256), unique=True, index=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    grade = db.Column(db.String(64))
    role_id = db.Column(db.Integer)
    is_display = db.Column(
        db.Boolean(), nullable=False, server_default=sql.true())
    date_created = db.Column(
        db.DateTime, nullable=False, index=True,
        server_default=db.func.current_timestamp())

    account = db.relationship(
        'OJAccountModel',
        primaryjoin='UserModel.id==OJAccountModel.user_id',
        foreign_keys='[OJAccountModel.user_id]',
        backref=db.backref('user', lazy=True),
        lazy='dynamic')

    poj = db.relationship(
        'OJAccountModel',
        primaryjoin='and_(UserModel.id==OJAccountModel.user_id, OJAccountModel.oj_name=="poj")',
        foreign_keys='[OJAccountModel.user_id]',
        lazy=True,
        uselist=False)

    sdutoj = db.relationship(
        'OJAccountModel',
        primaryjoin='and_(UserModel.id==OJAccountModel.user_id, OJAccountModel.oj_name=="sdutoj")',
        foreign_keys='[OJAccountModel.user_id]',
        lazy=True,
        uselist=False)

    role = db.relationship(
        'RoleModel',
        primaryjoin='UserModel.role_id==RoleModel.id',
        foreign_keys='[UserModel.role_id]',
        backref=db.backref(
            'user',
            lazy='dynamic'),
        lazy=True)

    solutions = db.relationship(
        'SolutionModel',
        primaryjoin='UserModel.id==SolutionModel.user_id',
        foreign_keys='[SolutionModel.user_id]',
        backref=db.backref('user', lazy=True),
        lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def can(self, permissions):
        return (self.role is not None and
                (self.role.permissions & permissions) == permissions)

    def is_administrator(self):
        return self.can(Permission.ADMINISTER)

    def get_submit_date(self, problem_id):
        solution = self.solutions.filter_by(problem_id=problem_id).first()
        if not solution:
            return ''
        return solution.date_submit.strftime('%Y-%m-%d')

    def __repr__(self):
        return 'User %r' % self.username


class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False

    def is_administrator(self):
        return False


login_manager.anonymous_user = AnonymousUser
