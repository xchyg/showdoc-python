# coding=utf-8
from .base import BaseHandler


class IndexHandler(BaseHandler):

    def index(self):
        name = self.get_secure_cookie('user')
        token = self.get_secure_cookie('token')
        self.render('Index/index.html', name=name, token=token)
