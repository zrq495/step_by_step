# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from flask import (
    redirect,
    url_for
)
from flask.views import MethodView
from flask.ext.login import logout_user, login_required


class LogoutView(MethodView):

    @login_required
    def get(self):
        logout_user()
        return redirect(url_for('index.index'))
