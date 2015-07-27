# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from flask import Blueprint

from .login import LoginView
from .logout import LogoutView

bp_auth = Blueprint('auth', __name__)

bp_auth.add_url_rule(
    '/login',
    endpoint='login',
    view_func=LoginView.as_view(b'login'),
    methods=['get', 'post']
)

bp_auth.add_url_rule(
    '/logout',
    endpoint='logout',
    view_func=LogoutView.as_view(b'logout'),
    methods=['get']
)
