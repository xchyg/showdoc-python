# coding=utf-8
import time
import hashlib
from .base_model import BaseModel


class UserModel(BaseModel):

    def initialize(self):
        self.table = 'user'

    def getinfo(self, uid):
        return self.get_one('SELECT * FROM user WHERE uid=?', [uid])

    def add(self, data):
        return self.insert(data)

    def login(self, username, password):
        str_ = username + password + str(time.time())
        token = hashlib.md5(bytes(str_, encoding='utf-8')).hexdigest()
        data = {
            'cookie_token': token,
            'last_login_time': int(time.time())
        }
        where_data = [username, password]
        self.update(data, 'WHERE username=? AND password=?', where_data)
        return self.check_login(username, token)

    def check_login(self, name, token):
        return self.get_one('SELECT * FROM user WHERE username=? AND cookie_token=?', [name, token])

    def change_password(self, name, old_pw, new_pw):
        self.update({'password': new_pw}, 'WHERE username=? AND password=?', [name, old_pw])
