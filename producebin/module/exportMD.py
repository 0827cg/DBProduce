#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: cg
# time  : 2018-06-12

import os
from producebin.dbpObject import DBPObject
from producebin.utils.fileUtil import FileUtil
from producebin.utils.dictDo import DictItemLength
from producebin.utils.stringUtil import StringUtil
# from .exportModule import ExportModule

class ExportMD(DBPObject):

    '''
    describe: 导出md格式, markdown实现的文章中,需要两个'\n'才能实现换行
    '''

    _strFileNameSuffix = '.md'

    def __init__(self, strDirName, strFileName):    

        self.strFileName = strDirName + os.sep + strFileName + self._strFileNameSuffix
        self.fileUtilObj = FileUtil()
        self.showHint()
        self.fileUtilObj.checkAndCreateDir(strDirName)
        self.fileUtilObj.writerToFile(self.strFileName, "## 数据库结构文档\n\n")


    def writerTitle(self, strContent, intLevel=3):

        '''
        describe: 写标题
        :param strContent: 需要写入的内容
        :param intLevel: 几级标题,int类型, 默认3级
        :return:
        '''

        strMDContent = ('#' * int(intLevel)) + ' ' + strContent + '\n'
        try:
            self.fileUtilObj.writerFileContent(self.strFileName, strMDContent)
        except:
            self.logUtilObj.writerLog("执行方法writerTitle中writerFileContent(self.strFileName, strMDContent)时出错,"
                                      " self.strFileName = " + self.strFileName + ", strMDContent = " + strMDContent)

    def writerTable(self, listDictContent):

        '''
        describe: 根据表格内容的长度来写表格, 使用'&nbsp;'来填充美化表格,填写在表头两边,如: &nbsp;&nbsp;&nbsp;key&nbsp;&nbsp;&nbsp;
        根据自己的统计得到, 表头所在列的元素中,'&nbsp;'的个数等于长度最长的元素的长度*2时(左右两边对半),这个时候表格可观性较高, 即此方法就用这个算法实现
        :param listDictContent: list集合, 其元素为dict类型
        :return:  执行成功返回1, 不成功返回-1
        '''

        if len(listDictContent) != 0:

            strTitleContent = '| '
            strSpace = '&nbsp;'

            dictColumnMaxLength = DictItemLength(listDictContent).getColumnMaxLength()

            listTitle = list(listDictContent[0].keys())
            for strTitleItem in listTitle:
                strTitleContent += (strSpace * dictColumnMaxLength[strTitleItem]) + strTitleItem + (strSpace * dictColumnMaxLength[strTitleItem]) + ' |'

            strTwoRowContent = '|' + (' :---: |' * len(listTitle))

            try:
                self.fileUtilObj.writerFileContent(self.strFileName, strTitleContent)
                self.fileUtilObj.writerFileContent(self.strFileName, strTwoRowContent)
            except:
                self.logUtilObj.writerLog("执行方法writerTable中writerFileContent(self.strFileName, xxx)时出错, "
                                          "self.strFileName = " + self.strFileName +
                                          ", strTitleContent = " + strTitleContent +
                                          ", strTwoRowContent = " + strTwoRowContent)
                intResult = -1
                return intResult

            for listDictContentItem in listDictContent:

                strRowContent = '| '

                for listTitleItem in listTitle:
                    strContent = StringUtil.replaceAllChar(listDictContentItem[listTitleItem])
                    strRowContent += strContent + ' |'

                try:
                    self.fileUtilObj.writerFileContent(self.strFileName, strRowContent)

                except:
                    self.logUtilObj.writerLog("执行方法writerTable中"
                                              "writerFileContent(self.strFileName, strRowContent)时出错, "
                                              "self.strFileName = " + self.strFileName +
                                              ", strRowContent = " + strRowContent)
                    intResult = -1
                    return intResult

            self.fileUtilObj.writerFileContent(self.strFileName, '\n')
            intResult = 1
            return intResult

        else:
            self.logUtilObj.writerLog("writerTable()中listDictContent其长度为0, 导出表格失败, listDictContent = "
                                      + str(listDictContent))
            intResult = -1
            return intResult



    def writerTableUsePadding(self, listDictContent, intPadding):

        '''
        describe: 根据自定义间隔长度来写表格, 使用'&nbsp;'来填充美化表格,填写在表头两边,如: &nbsp;&nbsp;&nbsp;key&nbsp;&nbsp;&nbsp;
        这里以三个空格来写
        :param listDictContent: list集合, 其元素为dict类型
        :param intPadding: 间隔长度
        :return:
        '''


        if(len(listDictContent) != 0):

            strTitleContent = '| '
            strSpace = '&nbsp;'

            listTitle = list(listDictContent[0].keys())
            for strTitleItem in listTitle:
                strTitleContent += (strSpace * intPadding * 3) + strTitleItem + (strSpace * intPadding * 3) + ' |'

            strTwoRowContent = '|' + (' :---: |' * len(listTitle))

            try:
                self.fileUtilObj.writerFileContent(self.strFileName, strTitleContent)
                self.fileUtilObj.writerFileContent(self.strFileName, strTwoRowContent)
            except:
                self.logUtilObj.writerLog("执行方法writerTable中writerFileContent(self.strFileName, xxx)时出错, "
                                          "self.strFileName = " + self.strFileName +
                                          ", strTitleContent = " + strTitleContent +
                                          ", strTwoRowContent = " + strTwoRowContent)

            for listDictContentItem in listDictContent:

                strRowContent = '| '

                for listTitleItem in listTitle:
                    strContent = StringUtil.replaceAllChar(listDictContentItem[listTitleItem])
                    strRowContent += strContent + ' |'

                try:
                    self.fileUtilObj.writerFileContent(self.strFileName, strRowContent)
                except:
                    self.logUtilObj.writerLog("执行方法writerTable中"
                                              "writerFileContent(self.strFileName, strRowContent)时出错, "
                                              "self.strFileName = " + self.strFileName +
                                              ", strRowContent = " + strRowContent)

            self.fileUtilObj.writerFileContent(self.strFileName, '\n')

        else:
            self.logUtilObj.writerLog("writerTable()中listDictContent其长度为0, 导出表格失败, listDictContent = "
                                      + str(listDictContent))


    def showHint(self):

        '''
        describe: 仅为显示导出格式分割线
        :return:
        '''

        self.logUtilObj.writerLog('=====导出markdown=====')

    @staticmethod
    def showFileType():

        '''
        describe: 倒数类型后缀
        :return:
        '''

        return '.md'







