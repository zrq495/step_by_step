# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask_wtf import Form
from wtforms import PasswordField, StringField, BooleanField, SubmitField
from wtforms.validators import Required, Length


class LoginForm(Form):
    username = StringField(
        '邮箱或用户名', validators=[Required(), Length(1, 64)])
    password = PasswordField('密码', validators=[Required()])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')
