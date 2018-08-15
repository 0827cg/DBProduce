#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: cg
# time  : 2018-06-22

from producebin.utils.mysqlUtil import MySqlUtil
from producebin.utils.fileUtil import FileUtil
from producebin.dbpObject import DBPObject

class SearchValue(DBPObject):

    # 查找数据

    def __init__(self, dictMysqlMsg):

        self.dictMysqlMsg = dictMysqlMsg
        self.mysqlUtilObj = MySqlUtil(self.dictMysqlMsg)
        self.fileUtilObj = FileUtil()



    def getTotalTableName(self):

        # 获取所有表名字

        strGetTotalTableNameSql = ''

        try:
            strGetTotalTableNameSql = str(self.fileUtilObj.readFileContent('sql/getTotalTableName.sql')
                                      % ("'" + self.dictMysqlMsg['database'] + "'"))
        except:
            self.logUtilObj.writerLog('getTotalTableName()中拼接或者读取sql出错')

        listOrderDictTotalTableName = self.mysqlUtilObj.doSearchSql(strGetTotalTableNameSql)

        if(len(listOrderDictTotalTableName) == 0):
            self.logUtilObj.writerLog('查找所有表名: getTotalTableName()未查询到数据')

        return listOrderDictTotalTableName


    def getTableMsgByTableName(self, strTableName):

        # 根据表名来获取表结构

        strGetTableMsgSql = ''

        try:

            strGetTableMsgSql = str(self.fileUtilObj.readFileContent('sql/getTableMsgByTableName.sql')
                                % (("'" + self.dictMysqlMsg['database'] + "'"), ("'" + strTableName + "'")))
        except:
            self.logUtilObj.writerLog('getTableMsgByTableName()中拼接或者读取sql出错, strTableName = ' + strTableName)

        listOrderDictTableMsg = self.mysqlUtilObj.doSearchSql(strGetTableMsgSql)

        if(len(listOrderDictTableMsg) == 0):
            self.logUtilObj.writerLog('查询表结构getTableMsgByTableName()未查询到数据')

        return listOrderDictTableMsg


    def getTableDataChangeMsg(self, strTableName):

        # 根据表名来获取表的简单的变更信息

        strGetTableChangeMsgSql = ''

        try:
            strGetTableChangeMsgSql = str(self.fileUtilObj.readFileContent('sql/getTableDataChangeMsg.sql')
                                % (("'" + self.dictMysqlMsg['database'] + "'"), ("'" + strTableName + "'")))
        except:
            self.logUtilObj.writerLog('getTableDataChangeMsg()中拼接或者读取sql出错, strTableName = ' + strTableName)

        listOrderDictTableChangeMsg = self.mysqlUtilObj.doSearchSql(strGetTableChangeMsgSql)

        if(len(listOrderDictTableChangeMsg) == 0):
            self.logUtilObj.writerLog('查询表更改信息getTableDataChangeMsg()未查询到数据')

        return listOrderDictTableChangeMsg







