# coding=utf-8
from .base import BaseHandler


class CatHandler(BaseHandler):

    def edit(self):
        """
        编辑分类
        :return:
        """
        item_id = self.path_args[1]
        cats = self.cat.get_all_cats(item_id)
        return self.render('Catalog/edit.html', cats=cats, item_id=item_id)

    def save(self):
        """
        分类保存
        :return:
        """
        cat_name = self.get_argument('cat_name')
        order_id = self.get_argument('order_id')
        item_id = self.get_argument('item_id')
        parent_id = self.get_argument('parent_id')
        cat_id = self.get_argument('cat_id', False)
        if cat_id:
            data = {
                'cat_name': cat_id, 'parent_id': parent_id, 'order_id': order_id
            }
            self.cat.update(data, 'WHERE cat_id=?', [cat_id])
        else:
            self.cat.add(cat_name, parent_id, item_id, order_id)
        self.ret_json({"error_code": 0})
