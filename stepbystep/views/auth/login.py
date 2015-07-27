# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from flask import (
    request,
    redirect,
    url_for,
    flash,
    render_template
)

from flask.views import MethodView
from flask.ext.login import current_user, login_user

from .forms import LoginForm
from stepbystep.models import UserModel


class LoginView(MethodView):

    template = 'auth/login.html'

    def get(self):
        if current_user.is_authenticated():
            return redirect(url_for('index.index'))
        form = LoginForm()
        return render_template(self.template, form=form)

    def post(self):
        form = LoginForm()
        if not form.validate():
            return render_template(
                self.template, form=form)
        user = UserModel.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('index.index'))
        flash('用户名或密码不正确')
        return render_template(self.template, form=form)
