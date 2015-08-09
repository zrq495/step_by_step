#! -*- coding: utf-8 -*-

import sys
sys.path.append('../../')
import csv

from stepbystep import db


def import_user():
    from stepbystep.models import UserModel, OJAccountModel
    with open('stepbystep_user.csv', 'r') as users:
        for grade, account, name in csv.reader(users.read().splitlines()):
            if grade and account and name:
                user = UserModel.query.filter(UserModel.username == name).first()
                if not user:
                    user = UserModel(
                        username=name,
                        password='1234567890',
                        grade=grade)
                    db.session.add(user)
                    oj_account = OJAccountModel(
                        oj_name='sdut',
                        username=account)
                    oj_account.user = user
                    db.session.add(oj_account)
                    db.session.commit()
        db.session.commit()


if __name__ == '__main__':
    from stepbystep import app
    with app.app_context():
        import_user()
