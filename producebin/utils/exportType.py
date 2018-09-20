#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: cg
# time  : 2018-09-18

import os
from producebin.dbpObject import DBPObject
from producebin.utils.fileUtil import FileUtil
from producebin.module import *

class ExportType(DBPObject):

    # 获取导出模块的类型个数
    # 新增导出类型的类时, 需要为该类声明一个静态方法, 方法名为showFileType(), 内容即只需要返回一个该类处理的文件类型即可,例如
    '''
        @staticmethod
        def showFileType():

            return '.md'
    '''
    # 之后, 在module/__init__.py文件中进行引入这个类即可

    # 这个类中的方法getHasImportClassName和getTypeMsg不适用于打包, 打包exe之后, module/__init.py这个文件将会找不着
    # 所以需要另外使用别的方式
    # 这里添加了另一种方式, 即定义一个list集合listClassName, 其中的元素即类名, 另外添加了个方法getTypeMsgByList
    # 也就是如果增加了新的供导出类型的类, 则不仅需要在module/__init__.py文件中进行导入, 还得在此listClassName中进行添加类名, 这样才可
    # 这样的做法是为了如需要导出exe当个执行文件, 就可以直接找到这些供导出的类型
    # add in 2018-09-20 17:22

    listClassName = ['ExportMD']


    def getHasImportClassName(self):

        # 获取modules文件夹下的python文件中的类名
        # 严格来说, 是获取module/__init__.py中进行导入了的类名
        # 返回一个类名为元素的list集合

        listClassName = []

        strFilePath = self.strModuleFilePath + os.sep + '__init__.py'

        listFileContent = FileUtil().readFileContentLineList(strFilePath)

        for strLineContent in listFileContent:

            if 'import' in strLineContent and '#' not in strLineContent:

                listConent = strLineContent.split(' ')

                listClassName.append(listConent[-1])

        return listClassName


    def getTypeMsg(self):

        # 获取module文件夹中可供导出的文件类型
        # 返回一个list类型, 元素为类型名字, 即导出文件的后缀名

        listType = []

        listClassName = self.getHasImportClassName()

        for strClassName in listClassName:

            classObj = eval(strClassName)

            listType.append(classObj.showFileType())

        return listType


    def getTypeMsgByList(self, listClassName):

        # listClassName: list类型, 元素未存放提供导出类型实现的类名
        # 返回一个list类型, 元素为类型名字, 即导出文件的后缀名
        # add in 2018-09-20 17:14

        listType = []

        for strClassName in listClassName:

            classObj = eval(strClassName)

            listType.append(classObj.showFileType())

        return listType





