#!/usr/bin/env python
# coding=utf-8
import logging
import psycopg2


class Database(object):
    def __init__(self, user, password, database, host='127.0.0.1', port=5432):
        self.conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        self.cursor = self.conn.cursor()

    def select(self, sql, data=None):
        if data is None:
            data = []
        self.cursor.execute(sql, data)
        return self.cursor.fetchall()

    def get(self, sql, data=None):
        if data is None:
            data = []
        self.cursor.execute(sql, data)
        return self.cursor.fetchone()

    def insert(self, sql, data=None):
        if data is None:
            data = []
        try:
            self.cursor.execute(sql, data)
        except psycopg2.IntegrityError:
            self.conn.rollback()
            return False
        else:
            self.conn.commit()
            # oid
            return self.cursor.lastrowid

    def query(self, sql, data=None):
        if data is None:
            data = []
        try:
            self.cursor.execute(sql, data)
        except psycopg2.IntegrityError:
            self.conn.rollback()
            return False
        else:
            self.conn.commit()
            # 影响行数
            return self.cursor.rowcount

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    db = Database('postgres', '122896', 'example')
    _sql = 'select * from author'
    res = db.select(_sql)
    print(res)
