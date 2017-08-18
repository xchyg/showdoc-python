# coding=utf-8
import time
import hashlib
import logging
from .table import pgsql, users, now
from sqlalchemy.sql import select, and_


class UserModel(object):
    def getinfo(self, uid):
        s = select([users]).where(users.c.auto_id == uid)
        r = pgsql.execute(s)
        return r.fetchone()

    def add(self, data):
        i = users.insert()
        r = pgsql.execute(i, **data)
        return r.inserted_primary_key[0]

    def login(self, username, password):
        str_ = username + password + str(time.time())
        token = hashlib.md5(bytes(str_, encoding='utf-8')).hexdigest()
        s = users.update().where(and_(users.c.user_name == username, users.c.password == password)).values(token=token, last_login_time=now())
        r = pgsql.execute(s)
        if r.rowcount > 0:
            return self.check_login(username, token)
        return False

    def check_login(self, name, token):
        s = select([users.c.auto_id, users.c.user_name, users.c.token]).where(
            and_(users.c.user_name == name, token == token))
        r = pgsql.execute(s)
        return r.fetchone()

    def change_password(self, uid, new_pw):
        data = {
            'password': new_pw
        }
        s = users.update().where(users.c.auto_id == uid).values(**data)
        r = pgsql.execute(s)
        return r.rowcount
