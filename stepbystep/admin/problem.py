# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from .mixin import ModelViewMixin
from . import admin
from stepbystep.models import ProblemModel
from stepbystep import db


class ProblemAdmin(ModelViewMixin):

    column_list = ['oj_name', 'problem_id', 'category', 'date_created']
    column_filters = ['oj_name', 'problem_id']
    column_searchable_list = ['problem_id', 'oj_name']

    form_excluded_columns = ['date_created', 'category_id']

    def __init__(self, session, **kwargs):
        super(ProblemAdmin, self).__init__(ProblemModel, session, **kwargs)


admin.add_view(ProblemAdmin(
    db.session, name='题目列表', category='题目管理', url='problem'))
