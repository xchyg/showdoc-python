# coding=utf-8
import time
import sqlite3
from abc import ABCMeta, abstractmethod


class BaseModel(object, metaclass=ABCMeta):
    def __init__(self):
        self.conn = sqlite3.connect('app.db', timeout=10)
        self.conn.row_factory = sqlite3.Row
        self.curs = self.conn.cursor()
        self.cursor = self.curs
        self.table = None
        self.initialize()

    @abstractmethod
    def initialize(self):
        """初始化"""
        # 例如设定表名
        pass

    def get_one(self, sql, args=None):
        """
        获取一条数据库记录
        :param sql: 查询语句。 如需要参数，使用 ? 占位
        :param args: 参数数组
        :return:
        """
        if args is None:
            args = []
        return self.cursor.execute(sql, args).fetchone()

    def get_all(self, sql, args=None):
        """
        获取全部数据库记录
        :param sql: 查询语句。 如需要参数，使用 ? 占位
        :param args: 参数数组
        :return:
        """
        if args is None:
            args = []
        return self.cursor.execute(sql, args).fetchall()

    def insert(self, data):
        """
        插入一条数据
        :param data: 字段与值 {column_name: value， }
        :return: 自增id
        """
        columns = []
        values = []
        temp = []
        for col, val in data.items():
            columns.append(col)
            values.append(val)
            temp.append('?')
        columns = ','.join(columns)
        temp = ','.join(temp)
        sql = 'INSERT INTO {} ({}) VALUES ({})'.format(self.table, columns, temp)
        self.curs.execute(sql, values)
        self.conn.commit()
        return self.curs.lastrowid

    def update(self, data, where_sql, where_data=None):
        """
        更新数据
        :param data:  字段与值 {column_name: value， }
        :param where_sql: 条件语句， 可使用 ？ 占位参数。WHERE id=?
        :param where_data: 条件语句的参数, [10]
        :return:
        """
        if where_data is None:
            where_data = []
        columns = []
        values = []
        temp = []
        for col, val in data.items():
            columns.append(col)
            values.append(val)
            temp.append('{}=?')
        temp = ','.join(temp)
        sql = 'UPDATE {} SET {} {}'.format(self.table, temp, where_sql).format(*columns)
        values.extend(where_data)
        self.cursor.execute(sql, values)
        self.conn.commit()

    @staticmethod
    def now():
        return int(time.time())
