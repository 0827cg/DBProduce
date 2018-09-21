#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: cg
# time  : 2018-06-08

import os
import time
from producebin.dbpObject import DBPObject


class FileUtil(DBPObject):

    # 读取文件类

    def readFileContent(self, strInputFileName):

        # 读取普通文件内容并返回
        # 每次只读取1000字节
        # strInputFileName: 需要读取的文件存放路径
        # 返回一个字符串类型, 为文件内容

        strFileContent = ''

        if os.path.exists(strInputFileName):

            with open(strInputFileName, 'r', encoding='utf-8') as fileObj:

                while fileObj.readable():
                    strFileContentItem = fileObj.read(1000)
                    if strFileContentItem != '':
                        strFileContent += strFileContentItem
                    else:
                        break
        else:
            self.logUtilObj.writerLog(strInputFileName + '文件不存在')

        return strFileContent


    def readFileContentLine(self, strInputFileName):

        # 读取普通文件内容并返回
        # 一行一行读取
        # strInputFileName: 需要读取的文件存放路径
        # 返回一个字符串类型, 为文件全部内容

        strFileContent = ''

        if os.path.exists(strInputFileName):

            with open(strInputFileName, 'r', encoding='utf-8') as fileObj:

                while fileObj.readable():
                    strFileContentItem = fileObj.readline()
                    if strFileContentItem != '':
                        strFileContent += strFileContentItem
                    else:
                        break

        else:
            self.logUtilObj.writerLog(strInputFileName + '文件不存在')

        return strFileContent


    def readFileContentLineList(self, strFileName):

        # 逐行读取普通文件内容, 添加进入list集合中并返回
        # 一行一行读取
        # strFileName: 需要读取的文件存放路径
        # 返回一个list集合, 元素为每一行的内容
        # add in 2018-09-18 16:57

        listFileContent = []

        if os.path.exists(strFileName):

            with open(strFileName, 'r', encoding='utf-8') as fileObj:

                while fileObj.readable():
                    strFileContentItem = fileObj.readline()
                    if strFileContentItem != '':
                        listFileContent.append(strFileContentItem)
                    else:
                        break

        else:
            self.logUtilObj.writerLog(strFileName + '文件不存在')

        return listFileContent



    @staticmethod
    def getLastContentForSmall(strFileName):

        # 读取文件的最后一行
        # 给小的文件使用
        # add in 2018-07-05

        with open(strFileName, 'rb') as fileObj:

            for strLine in fileObj.readlines():
                pass

        return(strLine.decode())

    @staticmethod
    def getLastContentForLarge(strFileName):

        # 读取文件的最后一行
        # 给大文件使用
        # add in 2018-07-05

        with open(strFileName, 'rb') as fileObj:
            fileObj.seek(-2, os.SEEK_END)

            while fileObj.read(1) != b'\n':
                fileObj.seek(-2, os.SEEK_CUR)

            return fileObj.readline().decode()

    @staticmethod
    def tailContent(strFileName):

        # 实现的功能类似tail -f命令读取内容
        # add in 2018-08-03
        # 返回迭代器
        # 使用内容方式
        '''
        for strContent in self.tailContent(strFileName):
            print(strContent)
        :param strFileName:
        :return: yield
        '''

        with open(strFileName, 'rb') as fileObj:
            pos = fileObj.seek(0, os.SEEK_END)
            print(pos)

            try:

                while True:
                    # currentPos = fileObj.seek(0, os.SEEK_END)
                    # print(currentPos)
                    #
                    # if currentPos > pos:
                    #     pos = fileObj.seek(0, os.SEEK_END)
                    #     continue

                    time.sleep(0.02)


                    strLineContent = fileObj.readline()
                    if not strLineContent:
                        continue
                    else:
                        # print(strLineContent)
                        yield strLineContent.decode('utf-8').strip('\n')
            except KeyboardInterrupt:
                pass

    @staticmethod
    def writerFileContent(strFileName, strContent, whetherAdd=True):

        # 写入文件
        # whetherAdd: 是否换行,默认换行

        if whetherAdd & True:
            with open(strFileName, 'a', encoding='utf-8') as fileObj:
                fileObj.write(strContent + '\n')
        else:
            with open(strFileName, 'a', encoding='utf-8') as fileObj:
                fileObj.write(strContent)

    @staticmethod
    def writerToFile(strFileName, strContent, whetherAdd=True):

        # 写入内容到指定文件
        # 这里的whetherAdd表示是否清空追加
        # 如果为True则会清空追加

        if whetherAdd & True:
            with open(strFileName, 'w', encoding='utf-8') as fileObj:
                fileObj.write(strContent)

        else:
            with open(strFileName, 'a', encoding='utf-8') as fileObj:
                fileObj.write("\n" + strContent)


    def checkAndCreateDir(self, strDirName):

        if not os.path.exists(strDirName):
            os.makedirs(strDirName)
            self.logUtilObj.writerLog(strDirName + "文件夹不存在,已自动创建")
