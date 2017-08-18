# coding=utf-8
import time
from .table import pgsql, category, now
from sqlalchemy.sql import select, and_


class CatModel():
    def add(self, cat_name, parent_id, item_id, order_id):
        i = category.insert()
        cat = {
            'cat_name': cat_name,
            'parent_id': parent_id,
            'item_id': item_id,
            'order_id': order_id,
            'addtime': now()
        }
        r = pgsql.execute(i, **cat)
        return r.inserted_primary_key[0]

    def get_cats(self, item_id, pid=0):
        s = select([category]).where(and_(category.c.item_id == item_id, category.c.parent_id == pid))
        r = pgsql.execute(s)
        return r.fetchall()

    def get_all_cats(self, item_id):
        s = select([category]).where(category.c.item_id == item_id)
        r = pgsql.execute(s)
        return r.fetchall()
