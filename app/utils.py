#!/usr/bin/env python
# coding=utf-8


class StdDict(object):
    """
    方便前台使用 Data.key 形式访问字段的值
    """

    def __init__(self, D):
        """
        :param D: dict
        """
        self.d = D

    def __getattr__(self, item):
        """
        访问不存在的 attribute 时
        :param item:
        :return:
        """
        return self.d[item]
