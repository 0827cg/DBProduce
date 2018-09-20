#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: cg
# time  : 2018-08-06

import os
import configparser
from producebin.utils.configMsg import ConfigMsg


class ConfigureUtil:

    # .conf为后缀的文件操作类, 这里用来操作配置文件

    def __init__(self, logUtilObj, strDir, strFileName):

        self.logUtilObj = logUtilObj
        self.strDir = strDir
        self.strFileName = strFileName

        self.configMsgObj = ConfigMsg()

        # self.fileUtilObj = FileUtil()
        # self.strRootPath = os.getcwd()
        # self.configParserObj = configparser.ConfigParser(allow_no_value=True, delimiters=':')


    def initConfig(self, configParserObj):

        # 初始化配置文件
        # configParserObj: configparser的对象

        # self.fileUtilObj.checkAndCreateDir(self.strDir)
        # if not os.path.exists(self.strDir+self.strFileName):
        #     self.logUtilObj.writerLog('将初始化配置文件')

        configParserObj.add_section(self.configMsgObj.strExportSessionName)

        configParserObj.set(self.configMsgObj.strExportSessionName, self.configMsgObj.strExportDescribe)
        configParserObj.set(self.configMsgObj.strExportSessionName, self.configMsgObj.strFilePathKey,
                            self.configMsgObj.strFilePathValue)
        configParserObj.set(self.configMsgObj.strExportSessionName, self.configMsgObj.strFileNameKey,
                            self.configMsgObj.strFileNameValue)
        configParserObj.set(self.configMsgObj.strExportSessionName, self.configMsgObj.strFileTypeKey,
                            self.configMsgObj.strFileTypeValue)

        configParserObj.add_section(self.configMsgObj.strConSessionName)

        configParserObj.set(self.configMsgObj.strConSessionName, self.configMsgObj.strConnectionDescribe)
        configParserObj.set(self.configMsgObj.strConSessionName, self.configMsgObj.strHostKey,
                            self.configMsgObj.strHostValue)
        configParserObj.set(self.configMsgObj.strConSessionName, self.configMsgObj.strPortKey,
                            self.configMsgObj.strPortValue)
        configParserObj.set(self.configMsgObj.strConSessionName, self.configMsgObj.strUserKey,
                            self.configMsgObj.strUserValue)
        configParserObj.set(self.configMsgObj.strConSessionName, self.configMsgObj.strPassWordKey,
                            self.configMsgObj.strPassWordValue)


        with open(self.strDir + self.strFileName, 'w', encoding='utf-8') as configureFile:
            configParserObj.write(configureFile, space_around_delimiters=True)

        self.logUtilObj.writerLog('配置文件已初始化完成(' + self.strDir + self.strFileName + ')')
        # else:
        #     self.logUtilObj.writerLog('配置文件已经存在(' + self.strDir + self.strFileName + ')')


    def checkAndInitConfigure(self, configParserObj):

        # 检测配置文件是否存在, 若存在则比执行创建, 若不存在则初始化创建
        # configParserObj: configparser的对象

        if not os.path.exists(self.strDir + self.strFileName):
            self.initConfig(configParserObj)
        else:
            self.logUtilObj.writerLog('配置文件已经存在(' + self.strDir + self.strFileName + ')')


    def getConfig(self, configParserObj):

        '''
        读取配置文件内容, 注释了不读取，值为空会读取, 读取写入的key名字全部小写
        :param configParserObj: configparser的对象
        :return: 返回一个字典
        '''

        dictConfMsg = {}
        if os.path.exists(self.strDir + self.strFileName):
            configParserObj.read(self.strDir + self.strFileName)
            try:
                listSectionName = configParserObj.sections()
            except:

                self.logUtilObj.writerLog("读取配置文件出错")
            else:
                for sectionItem in listSectionName:

                    listKeyName = configParserObj.options(sectionItem)
                    sectionObj = configParserObj[sectionItem]

                    if len(listKeyName) != 0:
                        for keyItem in listKeyName:

                            if '#' not in keyItem:

                                valueItem = sectionObj[keyItem]
                                if valueItem is None:
                                    dictConfMsg[sectionItem] = listKeyName
                                else:
                                    dictConfMsg[keyItem] = valueItem
                            else:
                                continue
                    else:
                        dictConfMsg[sectionItem] = ''
        self.logUtilObj.writerLog('配置文件中读取到的配置有: ' + str(dictConfMsg))
        return dictConfMsg

    def updateConfigSingleKey(self, configParserObj, strSessionName, strKey, strValue):

        '''
        修改改配置文件, 针对单个key
        :param configParserObj: configparser的对象
        :param strSessionName: 需要更改的strKey对应的上一级名字
        :param strKey: 需要更改的key
        :param strValue: 需要更改的strKey的值
        :return:
        '''

        try:
            configParserObj.set(strSessionName, strKey, strValue)
            with open(self.strDir + self.strFileName, 'w', encoding='utf-8') as configureFile:
                configParserObj.write(configureFile, space_around_delimiters=True)
        except:
            self.logUtilObj.writerLog('更新修改出错: [' + strSessionName + ']' + strKey + ' = ' + strValue)
        else:
            self.logUtilObj.writerLog('已更新修改: [' + strSessionName + ']' + strKey + ' = ' + strValue)


    def updateConfigSingleSession(self, configParserObj, strSessionName, dictMsg):

        # 修改配置文件, 针对单个session块
        # configParserObj: configparser的对象
        # strSessionName: 块名字
        # dictMsg: 块对应的新内容, 字典类型
        configParserObj.read(self.strDir + self.strFileName)
        try:
            for strKey, strValue in dictMsg.items():
                configParserObj.set(strSessionName, strKey, strValue)

            with open(self.strDir + self.strFileName, 'w', encoding='utf-8') as configureFile:
                configParserObj.write(configureFile, space_around_delimiters=True)
        except:
            self.logUtilObj.writerLog('更新修改出错')
        else:
            self.logUtilObj.writerLog('已经更新修改: [' + strSessionName + ']配置块')


    def checkConfigHasExist(self, configParserObj, strSession, listKey):

        # 检测判断配置文件中是否存在session块配置信息,及配置信息的key是否完全

        '''

        :param configParserObj: configparser的对象
        :param strSession: 块名字
        :param listKey: list类型, 其元素为strSession块中的配置项的key名字
        :return: 1: 检查的配置项存在, -1: session配置块存在, 但缺少某项key, -2: session配置块不存在
        '''

        intIndex = 0

        configParserObj.read(self.strDir + self.strFileName)
        if configParserObj.has_section(strSession):

            for strKeyItem in listKey:
                if not configParserObj.has_option(strSession, strKeyItem):
                    self.logUtilObj.writerLog('配置文件中的' + strSession + '配置中' + strKeyItem + '的配置项不存在')
                    intIndex = -1
                else:
                    intIndex = 1
                    pass
        else:
            intIndex = -2
            self.logUtilObj.writerLog('配置文件中不存在' + strSession + '的配置块')

        return intIndex


    @staticmethod
    def getCustomizeConfigParserObj():

        # 返回一个实例化的configparser对象
        # 实例化时参数可改
        # 参数的配置需要根据自己的需求

        return configparser.ConfigParser(allow_no_value=True, delimiters=':')










