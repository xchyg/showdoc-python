# coding=utf-8
from app import consts
from .base import BaseHandler

import logging


class ItemHandler(BaseHandler):
    def index(self):
        uid = self.get_current_user()[0]
        data = self.item.get_all(uid)
        return self.render('Item/index.html', data=data)

    def add(self):
        """
        添加栏目
        :return:
        """
        data = {'msg': ''}
        form = self.get_argument('form', False)
        if form:
            item_type = self.get_argument('item_type')
            item_name = self.get_argument('item_name')
            item_description = self.get_argument('item_description')
            password = self.get_argument('password')
            if item_name and item_type:
                uid = self.get_current_user()[0]
                self.item.add(item_type, item_name,
                              item_description, password, uid)
                return self.redirect('/item/index')
            else:
                data['msg'] = '项目名不可为空'
        return self.render('Item/add.html')

    def show(self):
        """
        展示栏目
        :return:
        """
        item_id = self.path_args[1]
        if item_id:
            item = self.item.get_item(item_id)
            if item:
                if int(item[2]) == consts.ITEM_TYPE_MULTI:
                    # 常规项目
                    page_id = self.get_argument('page_id', False)
                    cats = self.cat.get_cats(item_id)
                    pages = self.page.get_pages(item_id)
                    if len(pages) > 0:
                        page = self.page.get_page(page_id) if page_id else pages[0]
                    else:
                        page = {'page_id': -1, 'page_title': '空',
                                'page_content': ''}
                    return self.render('Item/show_regular.html', item=item, cats=cats, pages=pages, show_page=page)
                elif int(item[2]) == consts.ITEM_TYPE_SINGLE:
                    # 单页项目
                    page = self.page.get_single_page(item_id)
                    return self.render('Item/show_single_page.html', item=item, page=page)

            return self.redirect('/item/index')

    def edit(self):
        item_id = self.path_args[1]
        logging.info(item_id)
        form = self.get_argument('form', False)
        if form:
            item_name = self.get_argument('item_name', False)
            item_desc = self.get_argument('item_description', False)
            password = self.get_argument('password', False)
            self.item.edit(item_id, item_name, item_desc, password)
            return self.redirect('/item/index')
        else:
            item = self.item.get_item(item_id)
            logging.info(item)
            if item:
                return self.render('Item/edit.html', item=item)
            return self.die_message('数据未找到', '/item/index', '')

    def deli(self):
        """
        删除栏目
        :return:
        """
        item_id = self.path_args[1]
        self.item.deli(item_id)
        return self.die_message('操作成功', '/item/index', '')
