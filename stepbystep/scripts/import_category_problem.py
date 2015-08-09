#! -*- coding: utf-8 -*-

import sys
sys.path.append('../../')
import csv

from stepbystep import db


def import_category_problem():
    from stepbystep.models import ProblemModel, CategoryModel
    with open('stepbystep_sdut.csv', 'r') as problems:
        c0 = c1 = c2 = c3 = p = None
        c1_count = c2_count = c3_count = p_count = 0
        for c0, c1, c2, c3, p in csv.reader(problems.read().splitlines()):
            print c0, c1, c2, c3, p
            if c0:
                c0 = CategoryModel(
                    name=c0,
                    url=c0)
                db.session.add(c0)
                c1_count = 0
                c0_temp = c0
            else:
                c0 = c0_temp
            if c1:
                c1 = CategoryModel(
                    name=c1,
                    url=c1,
                    ordinal=c1_count)
                c1.parent = c0
                db.session.add(c1)
                c1_count += 1
                c2_count = 0
                c1_temp = c1
            else:
                c1 = c1_temp
            if c2:
                c2 = CategoryModel(
                    name=c2,
                    ordinal=c2_count)
                c2.parent = c1
                db.session.add(c2)
                c2_count += 1
                c3_count = 0
                c2_temp = c2
            else:
                c2 = c2_temp
            if c3:
                c3 = CategoryModel(
                    name=c3,
                    ordinal=c3_count)
                c3.parent = c2
                db.session.add(c3)
                c3_count += 1
                p_count = 0
                c3_temp = c3
            else:
                c3 = c3_temp
            if p:
                p = ProblemModel(
                    oj_name='sdut',
                    problem_id=p,
                    ordinal=p_count)
                p.category = c3
                db.session.add(p)
                p_count += 1
            db.session.commit()
        db.session.commit()


if __name__ == '__main__':
    from stepbystep import app
    with app.app_context():
        import_category_problem()
