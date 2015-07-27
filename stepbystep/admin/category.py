# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from .mixin import ModelViewMixin
from . import admin
from stepbystep.models import CategoryModel
from stepbystep import db


class CategoryAdmin(ModelViewMixin):

    column_list = ['name', 'url', 'parent', 'date_created']
    column_filters = ['name']
    column_searchable_list = ['name']

    form_excluded_columns = ['date_created', 'problems', 'parent_id']

    def __init__(self, session, **kwargs):
        super(CategoryAdmin, self).__init__(CategoryModel, session, **kwargs)


admin.add_view(CategoryAdmin(
    db.session, name='分类列表', category='分类管理', url='category'))
