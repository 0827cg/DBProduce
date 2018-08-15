#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: cg
# time  : 2018-06-08

import os
from producebin.utils.logUtil import LogUtil
from producebin.utils.contentUtil import ContentUtil
from producebin.utils.configureUtil import ConfigureUtil

class DBPObject(object):

    _strLogDirPath = 'logs' + os.sep
    strConfigDirPath = 'conf' + os.sep
    strConfigFileName = 'dbp.conf'


    logUtilObj = LogUtil(_strLogDirPath)
    contentUtilObj = ContentUtil(logUtilObj.strLogFileName)
    configureUtilObj = ConfigureUtil(logUtilObj, strConfigDirPath, strConfigFileName)
    configParserObj = configureUtilObj.getCustomizeConfigParserObj()


    # def setConnection(connectionObj):
    #     connectionMysqlObj = connectionObj
    #
    # @classmethod
    # def getConnection(cls):
    #     return cls.connectionMysqlObj



