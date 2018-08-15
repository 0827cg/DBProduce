#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: cg
# time  : 2018-08-14


class StringUtil:

    # 字符串操作类

    @staticmethod
    def replaceAllChar(strContent):

        # 字符串替换
        # 这里替换转义字符和一些markdown等关键字符
        # 如需添加替换字符, 则只需要在arrNeedReplace中添加元素即可
        # 该元素中的key表示需要替换的字符, value表示替换后的新字符

        arrNeedReplace = {'\t': ' ', '\n': ' ', '|': ' '}

        for itemOld, itemNew in arrNeedReplace.items():
            strContent = strContent.replace(itemOld, itemNew)

        return strContent