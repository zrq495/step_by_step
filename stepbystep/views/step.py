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

from stepbystep.models import CategoryModel


class StepView(MethodView):

    template = 'step.html'

    def _get_problems(self, parent):
        problems = parent.problems.all()
        children = parent.children.order_by(CategoryModel.ordinal).all()
        if not children and problems:
            return self.problems.extend(problems)
        if children:
            for child in children:
                self._get_problems(child)

    def get(self, parent, child):
        self.problems = []
        parent = CategoryModel.query.filter(CategoryModel.url == parent).first()
        child = CategoryModel.query.filter(CategoryModel.url == child).first()
        self._get_problems(child)
        if child.parent == parent:
            return render_template(
                self.template, parent=parent, child=child,
                problems=self.problems)


bp_step = Blueprint('step', __name__)

bp_step.add_url_rule(
    '/<string:parent>/<string:child>/',
    endpoint='step',
    view_func=StepView.as_view(b'step'),
    methods=['get']
)
