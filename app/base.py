# coding=utf-8
import operator
import json
import tornado.web
from .model import UserModel
from .model import ItemModel
from .model import PageModel
from .model import CatModel


class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.user = UserModel()
        self.item = ItemModel()
        self.page = PageModel()
        self.cat = CatModel()

    def get(self, path, *args):
        if path:
            operator.methodcaller(path)(self)
        else:
            self.index()

    def post(self, path, *args):
        if path:
            operator.methodcaller(path)(self)
        else:
            self.index()

    def index(self):
        return self.redirect('/')

    def get_current_user(self):
        """
        获取当前用户
        :return:
        """
        name_ = self.get_secure_cookie('user')
        token_ = self.get_secure_cookie('token')
        if name_ and token_:
            name = str(name_, encoding='utf-8')
            token = str(token_, encoding='utf-8')
            return self.user.check_login(name, token)
        return False

    def ret_json(self, obj):
        """
        返回 json
        :param obj:
        :return:
        """
        str_ = json.dumps(obj)
        self.set_header('Content-type', 'application/json')
        return self.finish(str_)

    def die_message(self, msg, redirect, redirect_message):
        """
        进入信息展示(跳转)界面
        :param msg: 信息标题
        :param redirect: 跳转链接
        :param redirect_message: 具体信息
        :return:
        """
        data = {'msg': msg, 'redirect': redirect,
                'redirect_message': redirect_message}
        return self.render('Common/message.html', **data)

    def write_error(self, status_code, **kwargs):
        """
        捕捉错误
        :param status_code:
        :param kwargs:
        :return:
        """
        return self.die_message(str(status_code) + ' 错误', '/', '即将返回首页')
