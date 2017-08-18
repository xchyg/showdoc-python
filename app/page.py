# coding=utf-8
from .base import BaseHandler

import logging


class PageHandler(BaseHandler):

    def edit(self):
        """
        编辑页面
        :return:
        """
        page_id = self.path_args[1]
        page = self.page.get_page(page_id)
        if not page:
            return self.die_message('访问失败', '/', '文件不存在')
        level1_cat = self.cat.get_cats(page[1])
        level2_cat = []
        if level1_cat:
            level2_cat = self.cat.get_cats(page[1], level1_cat[0][2])
        return self.render('Page/edit.html', page=page, level1_cat=level1_cat, level2_cat=level2_cat, new_page=False)

    def save(self):
        """
        保存
        :return:
        """
        if not self.current_user:
            return self.ret_json({})
        cat_id = self.get_argument('cat_id')
        order_id = self.get_argument('order_id')
        page_content = self.get_argument('page_content')
        page_title = self.get_argument('page_title')
        page_comments = self.get_argument('page_comments')
        page_id = self.get_argument('page_id')
        item_id = self.get_argument('item_id')
        new_page = self.get_argument('new_page', False)
        if new_page:
            uid = self.current_user[0]
            self.page.add(uid, item_id, cat_id, page_title, page_content, page_comments, order_id)
        else:
            data = {
                'cat_id': cat_id,
                'order_id': order_id,
                'page_content': page_content,
                'page_title': page_title,
                'page_comments': page_comments
            }
            self.page.update(data, 'where page_id=? and item_id=?', [page_id, item_id])
        return self.ret_json({})

    def create(self):
        """
        创建页面
        :return:
        """
        item_id = self.path_args[1]
        page = {
            'item_id': item_id,
            'page_id': '',
            'page_content': '',
            'page_comments': '',
            'page_title': '',
        }
        level1_cat = self.cat.get_cats(item_id)
        level2_cat = []
        if level1_cat:
            level2_cat = self.cat.get_cats(item_id, level1_cat[0]['cat_id'])
        self.render('Page/edit.html', page=page, level1_cat=level1_cat, level2_cat=level2_cat, new_page=True)

    def single(self):
        page_id = self.path_args[1]
        page = self.page.get_page(page_id)
        if page:
            self.render('Page/single.html', page=page)
        else:
            self.die_message('访问失败', '/', '文件不存在')
            return

'''
`page_id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `author_uid` INTEGER DEFAULT 0,
    `author_username` TEXT,
    `item_id` INTEGER DEFAULT 0,
    `cat_id` INTEGER DEFAULT 0,
    `page_title` TEXT,
    `page_content` TEXT,
    `page_comments` TEXT,
    `order_id` INTEGER DEFAULT 99,
    `addtime` INTEGER DEFAULT 0
'''
