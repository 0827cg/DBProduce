#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: cg
# time  : 2018-07-04

import wx
import sys
import time
import operator
from win.connectDialog import ConnectDialog
from win.setDialog import SetDialog
from producebin.dbpObject import DBPObject
from win.dialogSelf import DialogSelf
from producebin.utils.fileUtil import FileUtil
from producebin.utils.threadWork import ThreadWork
from producebin.utils.configMsg import ConfigMsg
from producebin.bin.values import SearchValues
from producebin.bin.moduleValues import ModuleValues
from producebin.module.exportMD import ExportMD

class ProFrameControll(DBPObject):

    # 为主面板定义的事件响应类

    intGetDatabaseResult = 0
    strComboBoxChoice = ''

    def __init__(self, parentObj):

        self.parentObj = parentObj
        self.fileUtilObj = FileUtil()
        self.configMsgObj = ConfigMsg()
        self.searchValuesObj = SearchValues()

    def chooseMenuRun(self, eventObj):

        # eventObj:  事件对象
        # 为所有菜单中的按钮赋予相对应的执行方法

        intId = eventObj.GetId()
        menuObj = eventObj.GetEventObject()
        menuItemObj = menuObj.FindItemById(intId)
        strItemContent = menuItemObj.GetText()
        self.logUtilObj.writerLog('press in ' + str(intId) + '-' + strItemContent)

        if intId == 101:
            ConnectDialog(self.parentObj, 'connection mysql', 222, 280)

        elif intId == 102:
            SetDialog(self.parentObj, 'setting')

        elif intId == wx.ID_EXIT:
            dialogSelfObj = DialogSelf(self.parentObj, '退出', '确定退出.?')
            dialogSelfObj.showChooseUI()

        elif intId == 103:
            DialogSelf(self.parentObj, '关于', ' author: cg \n email: 1732821152@qq.com \n version: v1.0.0',
                       intHeight=143).showMessageUI()

        else:
            self.logUtilObj.writerLog('press in ' + str(intId) + '-未给id= ' + str(intId) + '的菜单组件分配方法')


    def chooseButtonRun(self, eventObj):

        # eventObj:  事件对象
        # 为所有界面中的按钮(button)赋予相对应的执行方法

        intId = eventObj.GetId()
        buttonObj = eventObj.GetEventObject()
        strPressContent = buttonObj.GetLabel()
        self.logUtilObj.writerLog('press in ' + str(intId) + '-' + strPressContent)

        if intId == 107:
            self.exportMsg()

            # 启动线程, 目的为循环读取文件内容并显示在面板
            # 现已废弃--time: 2018-08-02 16:18
            # 重新使用--time: 2018-08-03 14:44
            # threadSetLog = ThreadWork(self.parentObj)
            # self.parentObj.listThread.append(threadSetLog)
            # threadSetLog.start()

        else:
            self.logUtilObj.writerLog('press in ' + str(intId) + '-未给id= ' + str(intId) + '的按钮组件分配方法')

    def comboboxEvent(self, eventObj):

        # 为下拉框选择之后赋予响应事件的处理方法( when an item on the list is selected. )
        # eventObj: 响应事件对象

        # comboboxObj = eventObj.GetEventObject()
        # self.logUtilObj.writerLog(str(type(comboboxObj)))

        strComBoBoxChoice = str(eventObj.GetString())
        self.strComboBoxChoice = strComBoBoxChoice

        self.logUtilObj.writerLog('下拉框选择: ' + strComBoBoxChoice)
        self.setContentForCheckListBox(self.searchValuesObj.getTotalTablesName(strComBoBoxChoice))


    def comboboxCloseUp(self, eventObj):

        # 下拉选择框点击下拉后的响应事件处理

        # global intIndex

        comboboxObj = eventObj.GetEventObject()
        self.logUtilObj.writerLog(str(type(comboboxObj)))

        self.logUtilObj.writerLog('CloseUp self.intGetDatabaseResult: ' + str(self.intGetDatabaseResult))

        if self.searchValuesObj.connectionMysqlObj is not None:

            if self.intGetDatabaseResult != 1:
                intIndex = -1
            else:
                intIndex = 1

        else:
            intIndex = -2

        if intIndex == -1:

            self.logUtilObj.writerLog('下拉框赋值失败')
            DialogSelf(self.parentObj, 'error', '查找库失败, 请重试').showMessageUI()

        elif intIndex == -2:

            self.logUtilObj.writerLog('请先连接数据库')
            DialogSelf(self.parentObj, 'warning', '请先连接数据库').showMessageUI()
        else:
            pass


    def chooseRadioButton(self, eventObj):

        # eventObj:  事件对象
        # 为所有界面中的单选按钮(RadioButton)赋予相对应的执行方法

        intId = eventObj.GetId()
        radioButtonObj = eventObj.GetEventObject()
        strChooseContent = radioButtonObj.GetLabel()
        self.logUtilObj.writerLog('press in ' + str(intId) + '-' + strChooseContent)

        if intId == 104:
            self.selectAll(True)

        elif intId == 105:
            self.selectAll(False)

        else:
            self.logUtilObj.writerLog('press in ' + str(intId) + '-未给id= ' + str(intId) + '的当选组件分配方法')


    def frameFocus(self, eventObj):

        # 焦点检测事件
        # 当frame得到焦点时, 判断数据库是否有连接,若无连接则弹框

        # print(str(self.connectionMysqlObj) + '触发焦点')

        if self.searchValuesObj.connectionMysqlObj is not None:
            # print('已经连接数据库')

            if self.intGetDatabaseResult != 1:
                listValue = self.searchValuesObj.getDatabaseName()

                if listValue is not None:
                    self.setChoiceForComboBox(listValue)
                else:
                    self.logUtilObj.writerLog('未查找到库的数据')
        else:
            pass
            # print('未连接数据库')
            # DialogSelf(self.parentObj, 'test', '请先连接数据库').showMessageUI()


    def closeWin(self, eventObj):

        # 绑定关闭按钮
        # 先退出循环读取, 再停止线程, 最后关闭界面
        # 这里再添加断开数据库连接--add time: 2018-08-09

        self.contentUtilObj.setBooleanGetTailExit(True)
        self.logUtilObj.writerLog('booleanGetTailExit: ' + str(self.contentUtilObj.booleanGetTailExit))

        intLength = len(self.parentObj.listThread)

        try:

            for intIndex in range(intLength):
                self.parentObj.listThread[intIndex].stop()
                self.parentObj.listThread.pop(intIndex)
                intLength -= 1

            # while self.parentObj.listThread:
            #     threadNowObj = self.parentObj.listThread[0]
            #     threadNowObj.stop()
            #     self.parentObj.listThread.remove(threadNowObj)

        except Exception as error:
            self.logUtilObj.writerLog('线程关闭出错, 线程关闭出错, 程序可能卡死(建议杀死该进程)')
            self.logUtilObj.writerLog(str(error))
        else:

            time.sleep(0.3)
        finally:

            if self.searchValuesObj.connectionMysqlObj is not None:
                self.searchValuesObj.connectionMysqlObj.close()
                self.logUtilObj.writerLog('数据库连接已关闭')

            self.logUtilObj.writerLog('程序退出')
            sys.exit(0)


    def setChoiceForComboBox(self, arrItems):

        # 为主面板中的下拉框设置内容
        # arrItems: 需要显示到下拉框中的内容

        if len(arrItems) > 0:

            try:
                self.parentObj.comboBoxObj.SetItems(arrItems)
                self.parentObj.comboBoxObj.SetValue('选择数据库')

            except Exception as error:

                self.logUtilObj.writerLog('下拉选择框设置内容时出错,' + error)

            else:
                self.intGetDatabaseResult = 1

            self.logUtilObj.writerLog('已为主面板中的下拉框设置内容项, arrItems: ' + str(arrItems))
            self.logUtilObj.writerLog('总共元素个数为: ' + str(len(arrItems)))
        else:
            self.logUtilObj.writerLog('arrItems长度为0或值为空, 不进行设置')


        self.logUtilObj.writerLog('setChoiceForComboBox self.intGetDatabaseResult: ' + str(self.intGetDatabaseResult))


    def setContentForCheckListBox(self, arrItems):

        # 为主面板中的复选列表框设置内容
        # arrItems: 需要显示到复选列表框中的内容, 类型为list, 内容为其元素

        if len(arrItems) > 0:
            self.parentObj.checkListBoxObj.SetItems(arrItems)
            self.logUtilObj.writerLog('已为主面板中的复选列表框设置内容项, arrItems: ' + str(arrItems))
            self.logUtilObj.writerLog('总共元素个数为: ' + str(len(arrItems)))
        else:
            self.logUtilObj.writerLog('arrItems长度为0或值为空, 不进行设置')

    def exportMsg(self):

        # 导出
        # 这里先读取配置信息, 再获取选中的导出项, 之后导出

        intCheckRes = self.configureUtilObj.checkConfigHasExist(self.configParserObj,
                                                                self.configMsgObj.strExportSessionName,
                                                                self.configMsgObj.listFileKey)

        if intCheckRes == 1:
            dictConfig = self.configureUtilObj.getConfig(self.configParserObj)

            if self.searchValuesObj.connectionMysqlObj is not None:

                if self.strComboBoxChoice is '':
                    self.logUtilObj.writerLog('未选中具体数据库')
                    DialogSelf(self.parentObj, 'warning', '请先选择数据库').showMessageUI()
                else:
                    tupleCheckedStr = self.parentObj.checkListBoxObj.GetCheckedStrings()

                    if len(tupleCheckedStr) == 0:
                        self.logUtilObj.writerLog('未选中需要执行导出的表')
                        DialogSelf(self.parentObj, 'warning', '请先选择表').showMessageUI()
                    else:

                        if self.configMsgObj.strFileTypeKey in dictConfig:

                            strFileDir = dictConfig[self.configMsgObj.strFilePathKey]
                            strFileName = dictConfig[self.configMsgObj.strFileNameKey]
                            strFileType = dictConfig[self.configMsgObj.strFileTypeKey]

                            if operator.eq(strFileType, 'md'):

                                exportMDObj = ExportMD(strFileDir, strFileName)
                                ModuleValues(self.searchValuesObj).mdGenerateTuple(exportMDObj,
                                                                                   self.strComboBoxChoice, tupleCheckedStr)
                            else:
                                self.logUtilObj.writerLog('暂时不支持导出该类型')
                        else:
                            self.logUtilObj.writerLog('读取配置文件数据不全, 读取出错')
            else:
                self.logUtilObj.writerLog('未连接数据库')
                DialogSelf(self.parentObj, 'warning', '请先连接数据库').showMessageUI()

        else:
            self.logUtilObj.writerLog('配置文件中配置参数不全')


    def selectAll(self, booleanChoice):

        # 全选
        # booleanChoice: 选择的状态: true: 选中, false: 不选中

        intTotal = self.parentObj.checkListBoxObj.GetCount()

        for intIndex in range(intTotal):
            self.parentObj.checkListBoxObj.Check(intIndex, booleanChoice)

        if booleanChoice is True:
            self.logUtilObj.writerLog('全选个数: ' + str(intTotal))
        else:
            self.logUtilObj.writerLog('反选个数: ' + str(intTotal))


    def startThreadForLog(self):

        # 启动日志线程

        self.logUtilObj.writerLog('将启动子线程thread-log(读取渲染日志内容)')

        threadSetLog = ThreadWork(self.parentObj)
        self.parentObj.listThread.append(threadSetLog)
        threadSetLog.start()
        self.logUtilObj.writerLog('子线程thread-log已启动')


    def setLogMsgWinShow(self, strMsg):

        # 为日志显示框设置显示内容

        self.parentObj.textCtrlLogShowObj.AppendText(strMsg + '\n')


    def getSearchValues(self):

        return self.searchValuesObj

















