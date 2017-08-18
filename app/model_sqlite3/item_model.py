# coding=utf-8
import time
from app import consts
from .base_model import BaseModel
from .page_model import PageModel


class ItemModel(BaseModel):

    def initialize(self):
        self.table = 'item'

    def __init__(self):
        super().__init__()
        self.page = PageModel()

    def add(self, type_, name, desc, password, uid):
        data = {
            'item_type': type_,
            'item_name': name,
            'item_description': desc,
            'password': password,
            'uid': uid,
            'addtime': self.now()
        }
        id_ = self.insert(data)
        if int(type_) == consts.ITEM_TYPE_SINGLE and id_:
            self.page.add(author_uid=uid, item_id=id_, page_title=name)
        return id_

    def get_item(self, id_):
        return self.get_one('SELECT * FROM item WHERE item_id=?', [id_])

    def deli(self, item_id):
        self.curs.execute('DELETE FROM page WHERE item_id=?', [item_id])
        self.curs.execute('DELETE FROM category WHERE item_id=?', [item_id])
        self.curs.execute('DELETE FROM item WHERE item_id=?', [item_id])
        return self.conn.commit()

    def edit(self, item_id, item_name, item_desc, password):
        data = {
            'item_name': item_name,
            'item_description': item_desc,
            'password': password
        }
        self.update(data, 'WHERE item_id=?', [item_id])
