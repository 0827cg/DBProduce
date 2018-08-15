#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: cg
# time  : 2018-06-08


import datetime
import time
import os

class LogUtil:

    # 用来做日志记录

    def __init__(self, strLogDir):

        # strLogDir: 存放日志文件的文件夹路径(支持相对路径)
        # 日志文件的名字目前只以日期来命名

        self.strLogDir = strLogDir

        strToday = str(datetime.date.today())
        self.strLogFileName = self.strLogDir + strToday + ".log"

        self.checkAndCreateDir(self.strLogDir)


    def writerLog(self, strContent, whetherAdd=True):

        #写入文件
        # whetherAdd: 是否换行,默认换行

        if(whetherAdd & True):
            with open(self.strLogFileName, 'a', encoding='utf-8') as fileObj:
                fileObj.write(self.getDateTimeForLog() + strContent + '\n')
        else:
            with open(self.strLogFileName, 'a', encoding='utf-8') as fileObj:
                fileObj.write(self.getDateTimeForLog() + strContent)

        print(self.getDateTimeForLog() + strContent)


    def getTailLog(self, booleanDo):

        # 实现的功能类似tail -f命令读取日志内容
        # add in 2018-08-03
        # 返回迭代器

        with open(self.strLogFileName, 'rb') as fileObj:
            pos = fileObj.seek(0, os.SEEK_END)
            print(pos)

            try:

                while booleanDo:
                    print(pos)
                    # currentPos = fileObj.seek(0, os.SEEK_END)
                    # print(currentPos)
                    #
                    # if currentPos > pos:
                    #     pos = fileObj.seek(0, os.SEEK_END)
                    #     continue

                    strLineContent = fileObj.readline()
                    if not strLineContent:
                        continue
                    else:
                        # print(strLineContent)
                        yield strLineContent.decode('utf-8').strip('\n')
            except KeyboardInterrupt:
                pass


    def checkAndCreateDir(self, strDirName):

        if(not (os.path.exists(strDirName))):
            os.makedirs(strDirName)
            self.writerLog(strDirName + "文件夹不存在,已自动创建")
            self.writerLog("=================")
        else:
            self.writerLog('日志文件: ' + self.strLogFileName)

    def getDateTimeForLog(self):

        strTime = str(self.getTime("%Y-%m-%d %H:%M:%S"))
        return '[' + strTime + ']: '


    def getTimeForLog(self):

        strTime = str(self.getTime("%Y%m%d%H"))
        return strTime


    def getTime(self, strFormat):

        # 按照格式获取时间

        nowTime = time.localtime()
        strFormatTime = time.strftime(strFormat, nowTime)
        return strFormatTime


