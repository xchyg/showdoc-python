# coding=utf-8
import tornado.web
from .base import BaseHandler


class UserHandler(BaseHandler):

    def login(self):
        """
        登录
        :return:
        """
        data = {'msg': '', 'name': ''}
        form = self.get_argument('form', False)
        # 表单提交
        if form:
            username = self.get_argument('username', False)
            password = self.get_argument('password', False)
            data['name'] = username
            if username and password:
                user = self.user.login(username, password)
                if user:
                    self.set_secure_cookie('user', username, expires_days=5)
                    self.set_secure_cookie('token', user[2], expires_days=5)
                    self.die_message('登录成功', '/', '登录成功')
                    return
                else:
                    data['msg'] = '登录失败'
            else:
                data['msg'] = '用户名密码不能为空'

        self.render('User/login.html', info=data)

    def register(self):
        """
        注册
        :return:
        """
        data = {'msg': '', 'name': ''}
        form = self.get_argument('form', False)
        # 表单提交
        if form:
            username = self.get_argument('username', False)
            password1 = self.get_argument('password', False)
            password2 = self.get_argument('confirm_password', False)
            data['name'] = username
            if username and password1 and password1 == password2:
                data_ = {'user_name': username, 'password': password1}
                if self.user.add(data_):
                    self.die_message('注册成功', '/user/login', '注册成功')
                    return
                else:
                    data['msg'] = '注册失败'
            else:
                data['msg'] = '数据错误'

        self.render('User/register.html', info=data)

    @tornado.web.authenticated
    def logout(self):
        """
        退出登录
        :return:
        """
        self.set_secure_cookie('user', '', -1)
        self.set_secure_cookie('token', '', -1)
        self.redirect('/')

    @tornado.web.authenticated
    def setting(self):
        """
        设置
        :return:
        """
        data = {'msg': ''}
        form = self.get_argument('form', False)
        if form:
            user = self.get_current_user()
            pw = self.get_argument('password')
            new_pw = self.get_argument('new_password')
            if pw == user['password'] and new_pw:
                if self.user.change_password(user[0], new_pw):
                    self.set_secure_cookie('user', '', -1)
                    self.set_secure_cookie('token', '', -1)
                    self.redirect('/user/login')
                    return
                else:
                    data['msg'] = '更改失败'
            else:
                data['msg'] = '原密码不正确或新密码为空'

        return self.render('User/setting.html', data=data)
