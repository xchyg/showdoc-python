#!/usr/bin/env python
# coding=utf-8
import time

from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData, ForeignKey
from sqlalchemy import Column, Integer, String, Text


def now():
    return int(time.time())


engine = create_engine('postgresql+psycopg2://postgres:122896@localhost/example', encoding="utf-8")
metadata = MetaData()

users = Table('users', metadata,
              Column('auto_id', Integer, primary_key=True),
              Column('user_name', String(20)),
              Column('group_id', Integer, default=2),
              Column('nick', String(50)),
              Column('avatar', String(100)),
              Column('avatar_small', String(100)),
              Column('password', String(50)),
              Column('token', String(50)),
              Column('cookie_token_expire', Integer, default=0),
              Column('reg_time', Integer, default=0),
              Column('last_login_time', Integer, default=0)
              )

item = Table('item', metadata,
             Column('auto_id', Integer, primary_key=True),
             Column('item_type', Integer, default=1, nullable=False),
             Column('item_name', String(100), nullable=False),
             Column('item_description', Text),
             Column('password', String(30)),
             Column('uid', None, ForeignKey('users.auto_id')),
             Column('add_time', Integer)
             )

category = Table('category', metadata,
                 Column('auto_id', Integer, primary_key=True),
                 Column('cat_name', String(30)),
                 Column('parent_id', Integer, default=0),
                 Column('item_id', None, ForeignKey('item.auto_id')),
                 Column('order_id', Integer),
                 Column('add_time', Integer)
                 )

page = Table('page', metadata,
             Column('auto_id', Integer, primary_key=True),
             Column('uid', None, ForeignKey('users.auto_id')),
             Column('item_id', None, ForeignKey('item.auto_id')),
             Column('cat_id', Integer, default=0),
             Column('page_title', String(30)),
             Column('page_content', Text),
             Column('page_html', Text),
             Column('page_comments', String(100)),
             Column('order_id', Integer),
             Column('exit_time', Integer),
             Column('add_time', Integer)
             )

metadata.create_all(engine)
pgsql = engine.connect()
