#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: cg
# time  : 2018-06-22
# update time: 2018-08-09

from producebin.utils.mysqlUtil import MySqlUtil
from producebin.utils.fileUtil import FileUtil
from producebin.dbpObject import DBPObject
from sql.sqlSentence import SqlSentence

class SearchValues(DBPObject):

    '''
    describe: 获取数据库信息, 其中有些方法返回OrderedDict类型数据, 这种类型数据的遍历获取数据的方式和dict一样,
    不过就是这种OrderedDict类型数据是有序的
    将获取sql语句的方式更改为从代码中读取--update time:2018-08-17
    '''

    connectionMysqlObj = None

    def __init__(self):

        self.fileUtilObj = FileUtil()

    def getDatabaseName(self):

        '''
        describe: 查询链接的数据库中所有库的名字
        :return: 返回一个list类型数据, 元素为str类型库名字,
        '''

        listValue = []

        self.logUtilObj.writerLog('准备查询该连接的库下所有的数据库...')

        try:
            # strGetDatabaseSql = self.fileUtilObj.readFileContent('sql/getDatabaseName.sql')
            strGetDatabaseSql = SqlSentence().strDatabaseNameSql

            if strGetDatabaseSql == '':
                self.logUtilObj.writerLog('读取出错, sql内容为空')
                return None

        except Exception as error:
            self.logUtilObj.writerLog('getDatabaseName()中拼接或者读取sql出错' + str(error))
            return None

        else:
            listDictResultObj = MySqlUtil.doSearchSqlClass(self.connectionMysqlObj, strGetDatabaseSql)

            if len(listDictResultObj) != 0:

                # self.intGetDatabaseResult = 1

                self.logUtilObj.writerLog('查询得到的库的个数: ' + str(len(listDictResultObj)))

                for strContentItem in listDictResultObj:
                    for strKey, strValue in strContentItem.items():

                        listValue.append(strValue)

            else:
                self.logUtilObj.writerLog('getDatabaseName中传入的listDictResultObj长度为0或为空')
            return listValue


    def getTotalTablesName(self, strDBName):

        '''
        describe: 根据数据库名字查询该库下所有的表
        :param strDBName: 数据库名字
        :return: 返回一个lis类型数据, 元素为str类型的表名字
        '''

        listValue = []

        self.logUtilObj.writerLog('准备查询[strDBName=' + strDBName + ']该库下所有的表...')

        try:
            # strGetTableNameSql = self.fileUtilObj.readFileContent('sql/getTotalTableName.sql') % ("'" + strDBName + "'")
            strGetTableNameSql = SqlSentence().strTotalTableName % ("'" + strDBName + "'")

            if strGetTableNameSql == '':
                self.logUtilObj.writerLog('读取出错, sql内容为空')
                return None

        except Exception as error:
            self.logUtilObj.writerLog('getTotalTablesName()中拼接或者读取sql出错' + str(error))
            return None

        else:

            listDictResultObj = MySqlUtil.doSearchSqlClass(self.connectionMysqlObj, strGetTableNameSql)

            if len(listDictResultObj) != 0:

                self.logUtilObj.writerLog('查询得到的表个数: ' + str(len(listDictResultObj)))

                for strContentItem in listDictResultObj:
                    for strKey, strValue in strContentItem.items():
                        listValue.append(strValue)

            else:
                self.logUtilObj.writerLog('getTotalTablesName中传入的listDictResultObj长度为0或为空')

            return listValue


    def getTotalTablesNameForExport(self, strDBName):

        '''
        describe: 根据数据库名字查询该库下所有的表, 专门为导出功能提供
        :param strDBName: 数据库名字
        :return: 返回一个list类型数据 其元素为OrderedDict类型
        '''

        self.logUtilObj.writerLog('为导出,准备查询[strDBName=' + strDBName + ']该库下所有的表...')

        try:
            # strGetTotalTableNameSql = str(self.fileUtilObj.readFileContent('sql/getTotalTableName.sql')
            #                           % ("'" + strDBName + "'"))
            strGetTotalTableNameSql = SqlSentence().strTotalTableName % ("'" + strDBName + "'")

            if strGetTotalTableNameSql == '':
                self.logUtilObj.writerLog('读取出错, sql内容为空')
                return None

        except Exception as error:
            self.logUtilObj.writerLog('getTotalTableName()中拼接或者读取sql出错' + str(error))
            return None

        else:

            listOrderDictTotalTableName = MySqlUtil.doSearchSqlClass(self.connectionMysqlObj, strGetTotalTableNameSql)

            if len(listOrderDictTotalTableName) == 0:
                self.logUtilObj.writerLog('查找所有表名: getTotalTableName()未查询到数据')

            return listOrderDictTotalTableName


    def getSingleTableMsg(self, strDBName, strTableName):

        '''
        describe: 根据数据库及表名获取该表的信息
        :param strDBName: 库名字
        :param strTableName: 表名字
        :return: 返回一个list类型数据, 其元素为OrderedDict类型
        '''

        self.logUtilObj.writerLog('准备查询[strDBName=' + strDBName + ',strTableName=' + strTableName + ']的表信息...')

        # strGetTableMsgSql = ''
        try:

            # strGetTableMsgSql = self.fileUtilObj.readFileContent('sql/getTableMsgByTableName.sql') % (
            #     ("'" + strDBName + "'"), ("'" + strTableName + "'"))

            strGetTableMsgSql = SqlSentence().strTableMsgByTableName % (("'" + strDBName + "'"), ("'" + strTableName + "'"))

            if strGetTableMsgSql == '':
                self.logUtilObj.writerLog('读取出错, sql内容为空')
                return None

        except Exception as error:
            self.logUtilObj.writerLog('getSingleTableMsg()中拼接或者读取sql出错' + str(error))
            return None

        else:

            listDictResultObj = MySqlUtil.doSearchSqlClass(self.connectionMysqlObj, strGetTableMsgSql)

            return listDictResultObj



    def getSingleTableChangeMsg(self, strDBName, strTableName):

        '''
        describe: 根据库名和表名来获取表的简单的变更信息
        :param strDBName: 库名
        :param strTableName: 表名
        :return: 返回一个list类型数据, 其元素为OrderedDict类型
        '''

        self.logUtilObj.writerLog('准备查询[strDBName=' + strDBName + ',strTableName=' + strTableName + ']表的变更信息...')

        # strGetTableChangeMsgSql = ''

        try:
            # strGetTableChangeMsgSql = str(self.fileUtilObj.readFileContent('sql/getTableDataChangeMsg.sql')
            #                     % (("'" + strDBName + "'"), ("'" + strTableName + "'")))

            strGetTableChangeMsgSql = SqlSentence().strTableDataChangeMsgSql % (("'" + strDBName +
                                                                                 "'"), ("'" + strTableName + "'"))

            if strGetTableChangeMsgSql == '':
                self.logUtilObj.writerLog('读取出错, sql内容为空')
                return None

        except Exception as error:
            self.logUtilObj.writerLog('getTableDataChangeMsg()中拼接或者读取sql出错, strTableName = ' + strTableName)
            self.logUtilObj.writerLog(str(error))
            return None

        else:

            listDictTableChangeMsg = MySqlUtil.doSearchSqlClass(self.connectionMysqlObj, strGetTableChangeMsgSql)

            if len(listDictTableChangeMsg) == 0:
                self.logUtilObj.writerLog('查询表更改信息getTableDataChangeMsg()未查询到数据')

            return listDictTableChangeMsg