# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from flask import (
    request,
    redirect,
    url_for,
    current_app,
    render_template,
    Blueprint,
)
from flask.views import MethodView

from stepbystep.models import ProblemModel, CategoryModel


class StepPojView(MethodView):

    template = 'step.html'

    def get(self, parent, child):
        parent = CategoryModel.query.filter(CategoryModel.url == parent)
        child = CategoryModel.query.filter(CategoryModel.url == child)
        if child.parent == parent:
            return render_template(
                self.template, parent=parent, child=child)


bp_step = Blueprint('step', __name__)

bp_step.add_url_rule(
    '/<string:parent>/<string:child>/',
    endpoint='step',
    view_func=StepPojView.as_view(b'step'),
    methods=['get']
)
