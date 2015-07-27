# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from flask import redirect, url_for, request
from flask.ext.login import current_user
from flask.ext.admin import form, BaseView
from flask.ext.admin.contrib.sqla import ModelView


class Base(object):

    def is_accessible(self):
        return (current_user.is_authenticated()
                and current_user.is_administrator())

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('auth.login', next=request.url))


class ModelViewMixin(Base, ModelView):
    form_base_class = form.BaseForm
    column_display_pk = True
    form_extra_fields = None

    column_formatters = dict(
        date_created=(
            lambda v, c, m, p: m.date_created.strftime('%Y-%m-%d %H:%M:%S')),
    )


class BaseViewMixin(Base, BaseView):
    pass
