#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: cg
# time  : 2018-06-08

import pymysql.cursors
from producebin.dbpObject import DBPObject
from producebin.utils.coursorSelf import MyOrderedDictCursor
from producebin.utils.coursorSelf import MySSOrderedDictCursor


class DoMysql(DBPObject):

    # 连接数据库,返回一条连接

    def __init__(self, dictMsgForMysql):

        # 构造函数

        self.strHost = dictMsgForMysql.get('host')
        self.strPort = dictMsgForMysql.get('port')
        self.strUser = dictMsgForMysql.get('user')
        self.strPassWord = dictMsgForMysql.get('password')
        self.strDatabase = dictMsgForMysql.get('database')





    def connectionMySQL(self):

        # 连接数据库
        # 返回一个连接

        # 在connect()方法中去掉了参数cursorclass=pymysql.cursors.DictCursor
        # 这个参数会使得查询得到的结果为dict元素的list集合,
        '''
        例如
        [{'isNull': 'YES', 'isKey': '', 'columnType': 'int(11)', 'columnComment': '', 'columnName': 'append_user_id'},
        {'isNull': 'YES', 'isKey': '', 'columnType': 'int(11)', 'columnComment': '', 'columnName': 'append_time'},
        {'isNull': 'YES', 'isKey': '', 'columnType': 'int(11)', 'columnComment': '', 'columnName': 'modify_user_id'},
        {'isNull': 'YES', 'isKey': '', 'columnType': 'int(11)', 'columnComment': '', 'columnName': 'modify_time'}]
        :return:
        '''
        # 去掉之后, 其查询得到的输出就为双重的元组(tuple)类型的数据
        '''
        例如
        (('append_user_id', 'YES', 'int(11)', '', ''),
        ('append_time', 'YES', 'int(11)', '', ''),
        ('modify_user_id', 'YES', 'int(11)', '', ''), 
        ('modify_time', 'YES', 'int(11)', '', ''))
        :return:    
        '''

        connection = None

        try:
            connection = pymysql.connect(host=self.strHost, port=int(self.strPort), user=self.strUser,
                                         passwd=self.strPassWord, db=self.strDatabase,
                                         charset="utf8mb4", cursorclass=MyOrderedDictCursor)

        except:
            self.logUtilObj.writerLog('请重新检查数据库配置(可能配置出错或者网络出错)')

        if connection is not None:
            self.logUtilObj.writerLog("数据库已连接")

        return connection


    def connectionMysqlNoDB(self):

        # 不用库名来连接, 用来查看数据库或者创建数据库
        # add time: 2018-08-09 10:50

        connection = None

        try:
            connection = pymysql.connect(host=self.strHost, port=int(self.strPort), user=self.strUser,
                                         passwd=self.strPassWord, charset="utf8mb4", cursorclass=MyOrderedDictCursor)

        except:
            self.logUtilObj.writerLog('请重新检查数据库配置(可能配置出错或者网络出错)')

        # if connection is not None:
        #     self.logUtilObj.writerLog("数据库已连接")

        return connection