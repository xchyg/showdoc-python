# coding=utf-8
import time
from .base_model import BaseModel


class PageModel(BaseModel):

    def initialize(self):
        self.table = 'page'

    def add(self, uid, item_id, cat_id, title, page_content='', page_comments='', order_id=99):
        data = {
            'author_uid': uid,
            'item_id': item_id,
            'cat_id': cat_id,
            'page_title': title,
            'page_content': page_content,
            'page_comments': page_comments,
            'order_id': order_id
        }
        return self.insert(data)

    def get_single_page(self, item_id):
        """
        取得单页项目的页面
        :param item_id: 单页项目id
        :return:
        """
        sql = 'SELECT * FROM page WHERE item_id=?'
        return self.get_one(sql, [item_id])

    def get_page(self, page_id):
        """
        得到页面
        :param page_id: 页面id
        :return:
        """
        return self.get_one('select * from page where page_id=?', [page_id])

    def get_pages(self, item_id, cat_id=0):
        return self.get_all('select * from page where item_id=? and cat_id=?', [item_id, cat_id])
