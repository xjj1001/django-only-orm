import os

# 行是必须的
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_orm.settings")

from django_orm import migrate, make_migrations
from django_orm.app01.models import User, Record
# from demox import do_demo

import time
import random
import threading


def update():
    while True:
        try:
            obj = User.objects.first()
            obj.name = obj.name + 1
            obj.save()
            print("update:", object)
            # time.sleep(random.random()*0.5)
        except Exception as err:
            print("update:", "-" * 40)
            print(err)
        break


def create():
    while True:
        try:
            obj = User.objects.create(name=random.randint(0, 100))
            print("create:", obj)
            # time.sleep(random.random() * 0.5)
        except Exception as err:
            print("create:", "-" * 40)
            print(err)


def select():
    while True:
        try:
            print("select:", User.objects.all()[:5])
            # time.sleep(0.5)
        except Exception as err:
            print("select:", "-" * 40)
            print(err)
        break


def delete():
    while True:
        try:
            obj = User.objects.first()
            print("delete:", obj)
            obj.delete()
            # time.sleep(0.5)
        except Exception as err:
            print("delete:", "-" * 40)
            print(err)
        break


if __name__ == '__main__':
    # do_demo()
    # make_migrations("app01")
    # migrate("app01")
    # u = User.objects.create(name=111)
    # u.save()
    # u = User2.objects.create(name=222)
    # u.save()
    # print(len(User.objects.all()))
    # User.Meta.db_table = 'user2'
    Record._meta.db_table = 'user_record_20200606'  # 分表查询指定表名
    query = Record.objects.filter()
    for i in query:
        print(i.name)
    # # threading.Thread(target=update).start()
    # # threading.Thread(target=create).start()
    # threading.Thread(target=select).start()
    # # threading.Thread(target=delete).start()