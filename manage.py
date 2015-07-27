# -*- coding: utf-8 -*-

from stepbystep import app, db
from flask.ext.script import Manager, Server, Shell
from flask.ext.migrate import Migrate, MigrateCommand

from stepbystep.models import UserModel, RoleModel

manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, UserModel=UserModel, RoleModel=RoleModel)

manager.add_command("runserver", Server(host="0.0.0.0", port=5000))
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def deploy():
    from flask.ext.migrate import upgrade
    from stepbystep.models import RoleModel

    upgrade()

    RoleModel.insert_roles()


if __name__ == '__main__':
    manager.run()
