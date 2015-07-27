# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from config import config

app = Flask(__name__)
db = SQLAlchemy()
login_manager = LoginManager()

with app.app_context():
    config_name = os.getenv('STEPBYSTEP_CONFIG') or 'default'
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from .admin import admin
    admin.init_app(app)

    from .views import (
        bp_index,
        bp_auth,
    )

    app.register_blueprint(
        bp_index,
        url_prefix='/'
    )

    app.register_blueprint(
        bp_auth,
        url_prefix='/auth'
    )
