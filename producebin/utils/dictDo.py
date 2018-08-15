#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: cg
# time  : 2018-06-22

from producebin.dbpObject import DBPObject

class DictItemLength(DBPObject):

    # 统计list集合中dict类型元素的长度
    # 将其想象成一个表格

    # listDictObj: 可以是list类型,元素为dict的集合, 也可以是list类型, 元素为OrderedDict的集合
    # 如下

    '''
    [{'isNull': 'YES', 'columnName': 'append_user_id', 'columnComment': '', 'isKey': '', 'columnType': 'int(11)'},
    {'isNull': 'YES', 'columnName': 'append_time', 'columnComment': '', 'isKey': '', 'columnType': 'int(11)'},
    {'isNull': 'YES', 'columnName': 'modify_user_id', 'columnComment': '', 'isKey': '', 'columnType': 'int(11)'}]

    或

    [OrderedDict([('columnName', 'append_user_id'), ('isNull', 'YES'), ('columnType', 'int(11)'), ('isKey', ''), ('columnComment', '')]),
    OrderedDict([('columnName', 'append_time'), ('isNull', 'YES'), ('columnType', 'int(11)'), ('isKey', ''), ('columnComment', '')]),
    OrderedDict([('columnName', 'modify_user_id'), ('isNull', 'YES'), ('columnType', 'int(11)'), ('isKey', ''),('columnComment', '')])]
    '''


    def __init__(self, listDictObj):

        self.listDictObj = listDictObj

    def getColumnMaxLength(self):

        # 获取单个列中所有元素的最长元素长度
        # self.listDictObj的长度就是列中的元素个数+1(包括列名)
        # 返回一个dict类型的集合, key为列名, value为长度

        if isinstance(self.listDictObj, list):

            if isinstance(self.listDictObj[0], dict):

                dictResultObj = {}

                try:

                    listKey = self.listDictObj[0].keys()

                    for keyItem in listKey:
                        dictResultObj[keyItem] = len(keyItem)

                    for listDictItem in self.listDictObj:

                        for listKeyItem in listKey:

                            if len(str(listDictItem[listKeyItem])) > dictResultObj[listKeyItem]:
                                dictResultObj[listKeyItem] = len(str(listDictItem[listKeyItem]))
                except:
                    self.logUtilObj.writerLog('执行getColumnMaxLength()方法时出错, self.listDictObj: ' + str(self.listDictObj))

                self.logUtilObj.writerLog('得到的各列元素最长值为: ' + str(dictResultObj))

                return dictResultObj

            else:
                self.logUtilObj.writerLog('子元素不匹配, 需为dict类型')
        else:
            self.logUtilObj.writerLog(str(self.listDictObj) + ' :类型不匹配, 这里需为list类型')