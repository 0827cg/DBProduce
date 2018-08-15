#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: cg
# time  : 2018-06-22

import sys
from producebin.dbpObject import DBPObject
from producebin.bin.values import SearchValues
from producebin.module.exportMD import ExportMD
from producebin.utils.mysqlConnect import DoMysql
from producebin.bin.moduleValues import ModuleValues

class UseCommand(DBPObject):

    def __init__(self):

        self.searchValuesObj = SearchValues()
        self.operateDo()

    def operateDo(self):

        # while True:

        dictMysqlMsg = dict()

        self.logUtilObj.writerLog("请输入数据库信息('q to exit')")

        dictMysqlMsg['host'] = self.inputSelf("数据库地址(host address): ")
        dictMysqlMsg['port'] = int(self.inputSelf("端口号(port): "))
        dictMysqlMsg['user'] = self.inputSelf("用户名(user name): ")
        dictMysqlMsg['password'] = self.inputSelf("密码(password): ")

        self.logUtilObj.writerLog('准备连接数据库...')
        self.searchValuesObj.connectionMysqlObj = self.getConnectionMysql(dictMysqlMsg)

        if self.searchValuesObj.connectionMysqlObj is not None:

            listDBName = self.searchValuesObj.getDatabaseName()

            self.logUtilObj.writerLog('查找到的库如下, 请输入序号选择')
            self.showListAndIndex(listDBName)
            intChooseDBName = int(self.inputSelf('选择要查找的库(database): '))
            self.strDBName = listDBName[intChooseDBName - 1]
            self.logUtilObj.writerLog('选择的数据库为: ' + self.strDBName)


            # self.dictMysqlMsg['database'] = self.inputSelf("输入查找的库名(database): ")
            strSavePath = self.inputSelf("保存的路径(save path): ")
            strOutFileName = self.inputSelf("保存的文件名(output file name): ")
            intOutFileType = int(self.inputSelf("保存的文件类型(output file type):\n  1. markdown\t 2. text"))

            self.generatorValue(strSavePath, strOutFileName, intOutFileType)
        else:
            self.logUtilObj.writerLog('数据库连接出错, 程序退出')
            sys.exit(0)



    def inputSelf(self, strHint):

        # 用来接收用户的输入

        self.logUtilObj.writerLog('请输入' + strHint)
        strInput = input('>')

        if (strInput == 'q') or (strInput == 'Q'):
            self.logUtilObj.writerLog("程序退出")
            sys.exit()
        self.logUtilObj.writerLog('您的输入为: ' + strInput)

        return strInput


    def getConnectionMysql(self, dictMysqlMsg):

        # 连接数据库

        connectionObj = DoMysql(dictMysqlMsg).connectionMysqlNoDB()

        if connectionObj is None:
            self.logUtilObj.writerLog('连接出错')
        else:
            self.logUtilObj.writerLog('数据库已连接')
        return connectionObj


    def showListAndIndex(self, listMsg):

        # 显示数据让选择

        strContent = ''

        for intIndex in range(len(listMsg)):

            strContent += str(intIndex + 1) + ': ' + listMsg[intIndex] + '\t'
        self.logUtilObj.writerLog(strContent)


    def generatorValue(self, strSavePath, strOutFileName, intOutFileType):

        # 导出

        listTableName = self.searchValuesObj.getTotalTablesName(self.strDBName)

        if intOutFileType == 1:

            exportMDObj = ExportMD(strSavePath, strOutFileName)

            ModuleValues(self.searchValuesObj).mdGenerateTuple(exportMDObj, self.strDBName, listTableName)

        else:
            self.logUtilObj.writerLog('暂时不支持导出该类型')





