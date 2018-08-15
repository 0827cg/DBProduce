#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: cg
# time  : 2018-06-08

import platform
from producebin.utils.fileUtil import FileUtil
from producebin.dbpObject import DBPObject
from producebin.bin.useCommand import UseCommand
from win.produceUI import ProduceUI
from producebin.utils.process import ProcessCL

class OperateBin(DBPObject):

    # 程序引导入口, 根据当前系统是否支持界面程序运行来选择执行

    def __init__(self):

        self.chooseRun(self.__checkEnvironment())
        # self.chooseRun(0)

    def __checkEnvironment(self):

        # 本地执行的系统环境检测
        # linux, windows, mac
        # 其中linux系统可能有未安装窗口管理器, 就只能运行命令行

        global intIndex

        strPlatformMsg = platform.platform()

        if strPlatformMsg.find('Windows') != -1:
            self.logUtilObj.writerLog('检测到为windows系统' + '(' + strPlatformMsg + ')')
            intIndex = 1

        elif strPlatformMsg.find('Mac') != -1:
            self.logUtilObj.writerLog('检测到为mac系统' + '(' + strPlatformMsg + ')')
            intIndex = 2

        elif strPlatformMsg.find('Linux') != -1:
            self.logUtilObj.writerLog('检测到为linux系统' + '(' + strPlatformMsg + ')')
            intIndex = 3

            strCheckCL = 'runlevel'
            dictResult = ProcessCL().getResultAndProcess(strCheckCL)
            strOutResult = dictResult.get('stdout')

            if strOutResult is 'N 5':

                self.logUtilObj.writerLog('检测到该linux系统以运行桌面环境 ' + '(' + strOutResult + ')')
                intIndex = 4

            else:

                self.logUtilObj.writerLog('检测该到linux系统未运行桌面环境 ' + '(' + strOutResult + ')')
                intIndex = 0

        self.logUtilObj.writerLog('检测结果intIndex: ' + str(intIndex))

        return intIndex



    def chooseRun(self, intIndex):

        '''
        根据本地的环境来选择执行, 并先检测初始化配置文件
        :param intIndex: 环境检测的返回值
        :return: 0: 执行命令行操作,>0: 执行启动界面
        add time: 2018-08-07 09:42
        '''

        self.initConfig()
        if intIndex >= 1:

            self.logUtilObj.writerLog('执行启动界面...')
            ProduceUI(strTitle='DBProduct', intWidth=320, intHeight=480)

        elif intIndex == 0:
            self.logUtilObj.writerLog('执行命令行...')
            UseCommand()
        else:
            pass


    def initConfig(self):

        # 初始化配置文件

        FileUtil().checkAndCreateDir(self.strConfigDirPath)
        self.configureUtilObj.checkAndInitConfigure(self.configParserObj)





