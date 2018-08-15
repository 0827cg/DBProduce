#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: cg
# time  : 2018-08-08

import os

class ConfigMsg:

    # 配置文件的一些key名字和初始化的值

    strExportSessionName = 'ExportConfigure'
    strExporDescribe = '# export file name and path'
    strFilePathKey = 'path'
    strFileNameKey = 'name'
    strFileTypeKey = 'type'
    listFileKey = ['path', 'name', 'type']

    strFilePathValue = os.getcwd() + '/g/dngdosng/'
    strFileNameValue = 'test'
    strFileTypeValue = 'md'

    strConSessionName = 'MysqlConfigure'
    strConnectionDescribe = '# mysql connection'
    strHostKey = 'host'
    strPortKey = 'port'
    strUserKey = 'user'
    strPassWordKey = 'password'
    listConKey = ['host', 'port', 'user', 'password']

    strHostValue = ''
    strPortValue = ''
    strUserValue = ''
    strPassWordValue = ''