# coding=utf-8
from app import consts
from .table import pgsql, item, now
from .page_model import PageModel
from sqlalchemy.sql import select

import logging


class ItemModel(object):
    def __init__(self):
        self.page = PageModel()

    def add(self, type_, name, desc, password, uid):
        i = item.insert()
        data = {
            'item_type': type_,
            'item_name': name,
            'item_description': desc,
            'password': password,
            'uid': uid,
            'addtime': now()
        }
        r = pgsql.execute(i, **data)
        logging.info(r.inserted_primary_key)
        id_ = r.inserted_primary_key[0]
        if int(type_) == consts.ITEM_TYPE_SINGLE and id_:
            p = {'uid': uid, 'item_id': id_, 'cat_id': 0, 'page_title': name}
            self.page.add(p)
        return id_

    def get_item(self, id_):
        sel = [item.c.auto_id, item.c.item_name, item.c.item_type]
        s = select(sel).where(item.c.auto_id == id_)
        r = pgsql.execute(s)
        return r.fetchone()

    def get_all(self, id_):
        sel = [item.c.auto_id, item.c.item_name, item.c.item_description]
        s = select(sel).where(item.c.uid == id_)
        r = pgsql.execute(s)
        return r.fetchall()

    def edit(self, item_id, item_name, item_desc, password):
        data = {
            'item_name': item_name,
            'item_description': item_desc,
            'password': password
        }
        s = item.update().where(item.c.auto_id == item_id).values(**data)
        r = pgsql.execute(s)
        return r.rowcount
