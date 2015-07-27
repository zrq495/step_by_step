# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from flask import (
    request,
    redirect,
    url_for,
    render_template,
    Blueprint,
)
from flask.views import MethodView


class IndexView(MethodView):

    def get(self):
        return render_template('index.html')


bp_index = Blueprint('index', __name__)

bp_index.add_url_rule(
    '',
    view_func=IndexView.as_view(b'index'),
    methods=['GET']
)
