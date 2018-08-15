#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: cg
# time  : 2018-06-12
# update time: 2018-08-09

from producebin.utils.mysqlConnect import DoMysql
from producebin.dbpObject import DBPObject

class MySqlUtil(DBPObject):

    # 数据库操作类
    # 这里并未定义关闭连接的方法, 所以需要在调用这个类之后需要手动执行关闭

    def __init__(self, dictMsgForMysql):

        # dictMsgForMySql
        # 存放的字段
        # host
        # port
        # user
        # password
        # database
        if self.checkMsgWhetherExist(dictMsgForMysql) != -1:
            self.mysqlConnectionObj = self.getConnection(dictMsgForMysql)


    @classmethod
    def doSearchSqlClass(cls, mysqlConnectionObj, strSearchSql):

        # 单纯的执行查询语句
        # mysqlConnectionObj: 数据库连接对象
        # strSearchSql: 需要查询的语句
        # 返回一条list集合, 其元素类型为OrderedDict, 根据mysqlConnection中的连接类型
        # 以传入的连接对象来执行查询
        # add time: 2018-08-09

        cls.logUtilObj.writerLog("执行数据库查询语句: " + strSearchSql)

        listDictResultObj = []
        try:
            with mysqlConnectionObj.cursor() as cursor:
                cursor.execute(strSearchSql)
                listDictResultObj = cursor.fetchall()

            if len(listDictResultObj) == 0:
                cls.logUtilObj.writerLog("未查找到数据: " + strSearchSql)

        except:

            cls.logUtilObj.writerLog("查询出错:" + strSearchSql)

        cls.logUtilObj.writerLog("查到的数据: " + str(listDictResultObj))
        return listDictResultObj


    def doSearchSql(self, strSearchSql):

        # 单纯的执行查询语句
        # strSearchSql: 需要查询的语句
        # 返回一条list集合, 其元素类型为OrderedDict, 根据mysqlConnection中的连接类型

        self.logUtilObj.writerLog("执行数据库查询语句: " + strSearchSql)

        listDictResultObj = []
        try:
            with self.mysqlConnectionObj.cursor() as cursor:
                cursor.execute(strSearchSql)
                listDictResultObj = cursor.fetchall()

            if len(listDictResultObj) == 0:
                self.logUtilObj.writerLog("未查找到数据: " + strSearchSql)

        except:

            self.logUtilObj.writerLog("查询出错:" + strSearchSql)

        self.logUtilObj.writerLog("查到的数据: " + str(listDictResultObj))
        return listDictResultObj




    def getConnection(self, dictMsgForMysql):

        # 根据数据获取数据库连接

        return DoMysql(dictMsgForMysql).connectionMySQL()


    def getMsgForMysql(self, dictNeedRunMsg):

        # 获取连接mysql数据库所需要的数据，并判断是否完全
        # dictNeedRunMsg: 所有运行需要的配置, 包括mysql的
        # 返回一个dict类型的数据
        # 存放的字段
        # host
        # port
        # user
        # passwd
        # database

        dictMsgForMysql = {}

        for keyItem in dictNeedRunMsg:
            if ((keyItem == 'host') | (keyItem == 'port') |
                    (keyItem == 'user') | (keyItem == 'password') | (keyItem == 'database')):
                if dictNeedRunMsg.get(keyItem) != '':

                    dictMsgForMysql[keyItem] = dictNeedRunMsg.get(keyItem)
                else:
                    dictMsgForMysql.clear()
                    dictMsgForMysql['err'] = "Msg Incomplete"
                    break

        return dictMsgForMysql


    def checkMsgWhetherExist(self, dictMsgForMysql):

        # 判断传入来的dictMsgForMysql中配置信息是否完全
        # 数据配置不全则返回-1, 全则为一个大于0的整数
        # add in 2018-06-22

        listKey = ['host', 'user', 'password', 'port', 'database']
        intIndex = 0

        for listKeyItem in listKey:

            if (listKeyItem in dictMsgForMysql) and (dictMsgForMysql[listKeyItem]) != '':
                intIndex += 1
            else:
                intIndex = -1
                self.logUtilObj.writerLog('检测到数据库配置信息不全: ' + str(dictMsgForMysql))
                break

        return intIndex
