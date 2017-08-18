# coding=utf-8
import os
import tornado.ioloop
import tornado.web
import tornado.escape
import tornado.options
from tornado.options import define, options
from app import *

define("port", default=8888, help="run on the given port", type=int)


class HeaderModule(tornado.web.UIModule):
    def render(self):
        return self.render_string('Common/header.html')


class FooterModule(tornado.web.UIModule):
    def render(self):
        return self.render_string('Common/footer.html')


def main():
    tornado.options.parse_command_line()

    settings = {
        "login_url": "/user/login",
        'template_path': os.path.join(os.path.dirname(__file__), "templates"),
        'static_path': os.path.join(os.path.dirname(__file__), "static"),
        'cookie_secret': '61oETzKxQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo='
    }
    modules = {
        'Footer': FooterModule,
        'Header': HeaderModule
    }
    handlers = [
        (r"/(\w*)", IndexHandler),
        (r"/user/(\w*)", UserHandler),
        (r"/item/(\w*)", ItemHandler),
        (r"/item/(\w*)/(\d+)", ItemHandler),
        (r"/page/(\w*)", PageHandler),
        (r"/page/(\w*)/(\d+)", PageHandler),
        (r"/cat/(\w*)", CatHandler),
        (r"/cat/(\w*)/(\d+)", CatHandler),
    ]
    application = tornado.web.Application(handlers, ui_modules=modules, **settings)
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
