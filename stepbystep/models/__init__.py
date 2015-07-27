# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from .user import *  # noqa
from .account import *  # noqa
from .role import *  # noqa
from .category import *  # noqa
from .problem import *  # noqa

from stepbystep import db
db.configure_mappers()
