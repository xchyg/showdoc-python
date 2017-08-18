# coding=utf-8
import time
from .base_model import BaseModel


class CatModel(BaseModel):

    def initialize(self):
        self.table = 'category'

    def add(self, cat_name, parent_id, item_id, order_id):
        data = {
            'cat_name': cat_name,
            'parent_id': parent_id,
            'item_id': item_id,
            'order_id': order_id,
            'addtime': self.now()
        }
        return self.insert(data)

    def get_cats(self, item_id, pid=0):
        return self.get_all('select * from category where item_id=? and parent_id=?', [item_id, pid])

    def get_all_cats(self, item_id):
        """
        项目下所以分类
        :param item_id: 项目id
        :return:
        """
        return self.get_all('select * from category where item_id=?', [item_id])
