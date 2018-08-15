#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: cg
# time  : 2018-06-15

from pymysql.cursors import DictCursor
from pymysql.cursors import SSDictCursor
from collections import OrderedDict


class MyOrderedDictCursor(DictCursor):

    # 这个类是用作连接mysql时,使得执行查询语句之后得到的数据能有key并是有序的(依照查找顺序输出)
    # 这样查找得到的数据类型是个list集合, 元素类型是OrderedDict类型
    # 主要时看OrderedDict这个类模块
    # 这样写的依据详看pymysql的源代码

    dict_type = OrderedDict


class MySSOrderedDictCursor(SSDictCursor):

    # 跟上面的类时一样的作用, 得到的格式效果是一样的
    # SSDictCursor和DictCursor都继承与Cursor

    dict_type = OrderedDict





