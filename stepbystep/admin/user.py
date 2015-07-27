# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from wtforms import fields

from .mixin import ModelViewMixin
from . import admin
from stepbystep.models import UserModel, RoleModel
from stepbystep import db


class UserAdmin(ModelViewMixin):

    column_list = [
        'username', 'role', 'poj', 'sdut', 'date_created']
    column_filters = ['username']
    column_searchable_list = ['username']

    form_excluded_columns = [
        'password_hash', 'date_created', 'role_id', 'account']

    def __init__(self, session, **kwargs):
        super(UserAdmin, self).__init__(UserModel, session, **kwargs)

    def scaffold_form(self):
        form_class = super(UserAdmin, self).scaffold_form()
        form_class.password2 = fields.StringField('Password')
        return form_class

    def on_model_change(self, form, model):
        if len(model.password2):
            model.password = form.password2.data
        elif not model.password_hash:
            model.password = '12345678'


class RoleAdmin(ModelViewMixin):

    column_list = [
        'name', 'permissions', 'date_created']
    column_filters = ['name']
    column_searchable_list = ['name']

    form_excluded_columns = ['date_created']

    def __init__(self, session, **kwargs):
        super(RoleAdmin, self).__init__(RoleModel, session, **kwargs)


admin.add_view(UserAdmin(
    db.session, name='用户列表', category='用户管理', url='user'))
admin.add_view(RoleAdmin(
    db.session, name='角色列表', category='用户管理', url='role'))
