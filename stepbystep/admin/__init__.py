# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from flask.ext.admin import Admin, AdminIndexView as _AdminIndexView

from .mixin import Base


class AdminIndexView(Base, _AdminIndexView):
    pass


admin = Admin(
    name='StepByStep管理后台',
    index_view=AdminIndexView(name='首页'),
    template_mode='bootstrap3'
)

from . import user  # noqa
from . import problem  # noqa
from . import category  # noqa
