# coding=utf-8
from .table import pgsql, page, now
from sqlalchemy.sql import select


class PageModel(object):
    def add(self, uid, item_id, cat_id, title, page_content='', page_comments='', order_id=99):
        i = page.insert()
        data = {
            'uid': uid,
            'item_id': item_id,
            'cat_id': cat_id,
            'page_title': title,
            'page_content': page_content,
            'page_comments': page_comments,
            'order_id': order_id,
            'edit_time': now(),
            'add_time': now()
        }
        r = pgsql.execute(i, **data)
        return r.inserted_primary_key[0]

    def get_single_page(self, item_id):
        """
        取得单页项目的页面
        :param item_id: 单页项目id
        :return:
        """
        sel = [page.c.auto_id, page.c.item_id, page.c.cat_id, page.c.page_content]
        s = select(sel).where(page.c.item_id == item_id)
        r = pgsql.execute(s)
        return r.fetchone()

    def get_page(self, page_id):
        """
        得到页面
        :param page_id: 页面id
        :return:
        """
        sel = [page.c.auto_id, page.c.item_id, page.c.cat_id, page.c.page_title, page.c.page_content, page.c.page_html, page.c.page_comments]
        s = select(sel).where(page.c.auto_id == page_id)
        r = pgsql.execute(s)
        return r.fetchone()

    def get_pages(self, item_id, cat_id=0):
        s = select([page]).where(page.c.item_id == item_id, cat_id == cat_id)
        r = pgsql.execute(s)
        return r.fetchall()
