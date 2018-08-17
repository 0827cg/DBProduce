#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: cg
# time  : 2018-07-04

import wx
from producebin.dbpObject import DBPObject
from producebin.utils.configMsg import ConfigMsg
from producebin.utils.mysqlConnect import DoMysql
from win.dialogSelf import DialogSelf

class ConnectDialogControll(DBPObject):

    # 连接数据库的操作响应类

    def __init__(self, windowsObj, parentObj):

        self.windowsObj = windowsObj
        self.parentObj = parentObj

        self.configMsgObj = ConfigMsg()
        self.searchValuesObj = self.parentObj.proFrameControllObj.getSearchValues()

        self.__listKey = [self.configMsgObj.strHostKey,
                          self.configMsgObj.strPortKey,
                          self.configMsgObj.strUserKey,
                          self.configMsgObj.strPassWordKey]

    # 为输入连接数据库信息的面板定义的事件响应类

    def chooseButtonRun(self, eventObj):

        # eventObj:  事件对象
        # 为所有界面中的按钮(button)赋予相对应的执行方法

        intId = eventObj.GetId()
        buttonObj = eventObj.GetEventObject()
        strPressContent = buttonObj.GetLabel()
        self.logUtilObj.writerLog('press in ' + str(intId) + '-' + strPressContent)
        if intId == 205:
            self.logUtilObj.writerLog('断开前 self.intGetDatabaseResult: ' + str(self.parentObj.proFrameControllObj.intGetDatabaseResult))
            intCheck = self.checkWhetherNull(self.getContentFromWidgets())
            if intCheck == -1:
                self.logUtilObj.writerLog('请将数据库信息配置完全')
                DialogSelf(self.parentObj, 'warning', '请将数据库信息配置完全').showMessageUI()

            else:

                if '断开' in strPressContent:

                    if self.searchValuesObj.connectionMysqlObj is not None:
                        self.searchValuesObj.connectionMysqlObj.close()
                        self.searchValuesObj.connectionMysqlObj = None
                        self.parentObj.proFrameControllObj.intGetDatabaseResult = 0
                        DialogSelf(self.parentObj, 'ok', '数据库连接已断开').showMessageUI()
                        self.logUtilObj.writerLog('数据库连接已断开')

                        self.setContentSingleWidget(buttonObj, '测试连接')
                        self.windowsObj.buttonConformObj.Enable()

                        self.logUtilObj.writerLog('searchValuesObj.connectionMysqlObjself: ' + str(self.searchValuesObj.connectionMysqlObj))
                        self.logUtilObj.writerLog('断开后 self.intGetDatabaseResult: ' + str(
                            self.parentObj.proFrameControllObj.intGetDatabaseResult))

                else:
                    intResult = self.getConnectionForTest()
                    if intResult == 1:
                        DialogSelf(self.parentObj, 'ok', '数据库可正常连接').showMessageUI()
                    else:
                        DialogSelf(self.parentObj, 'error', '数据库连接出错').showMessageUI()

        elif intId == 206:

            intCheck = self.checkWhetherNull(self.getContentFromWidgets())
            if intCheck == -1:
                self.logUtilObj.writerLog('请将数据库信息配置完全')
                DialogSelf(self.parentObj, 'warning', '请将数据库信息配置完全').showMessageUI()
            else:

                connectionObj = self.getConnectionMysql()
                if connectionObj is not None:

                    # searchValuesObj = self.parentObj.proFrameControllObj.getSearchValues()
                    self.searchValuesObj.connectionMysqlObj = connectionObj
                    self.logUtilObj.writerLog('searchValuesObj.connectionMysqlObj: ' + str(self.searchValuesObj.connectionMysqlObj))
                    self.logUtilObj.writerLog('数据库连接成功')
                    self.saveContent()

                    self.windowsObj.EndModal(intId)

                else:
                    self.logUtilObj.writerLog('数据库连接失败')
                    DialogSelf(self.parentObj, 'error', '数据库连接出错').showMessageUI()


        elif intId == 207:
            self.windowsObj.EndModal(intId)

        else:
            self.logUtilObj.writerLog('press in ' + str(intId) + '-未给id= ' + str(intId) + '的按钮组件分配方法')


    def getConnectionMysql(self):

        # 连接数据库
        # 返回一条连接对象

        dictGetSaveMsg = self.getContentFromWidgets()

        connectionObj = DoMysql(dictGetSaveMsg).connectionMysqlNoDB()

        if connectionObj is None:
            self.logUtilObj.writerLog('连接出错')
        else:
            self.logUtilObj.writerLog('数据库已连接')
        return connectionObj


    def getConnectionForTest(self):

        # 测试连接数据库
        # return: 1: 已连接(可连接), -1: 连接出错

        connectionObj = self.getConnectionMysql()

        if connectionObj is None:
            intResult = -1
        else:
            intResult = 1
            connectionObj.close()
            self.logUtilObj.writerLog('连接已断开')

        return intResult


    def setContent(self):

        # 为连接数据库的弹框中的所有输入框设置内容

        intResult = self.configureUtilObj.checkConfigHasExist(self.configParserObj,
                                                              self.configMsgObj.strConSessionName,
                                                              self.__listKey)
        if intResult == 1:

            dictConnectionMsg = self.configureUtilObj.getConfig(self.configParserObj)
            self.windowsObj.textCtrlIpObj.SetValue(dictConnectionMsg[self.configMsgObj.strHostKey])
            self.windowsObj.textCtrlPortObj.SetValue(dictConnectionMsg[self.configMsgObj.strPortKey])
            self.windowsObj.textCtrlUserNameObj.SetValue(dictConnectionMsg[self.configMsgObj.strUserKey])
            self.windowsObj.textCtrlPasswdObj.SetValue(dictConnectionMsg[self.configMsgObj.strPassWordKey])
        else:
            self.logUtilObj.writerLog('未找到相应的配置参数, intResult: ' + str(intResult))


    @staticmethod
    def setContentSingleWidget(widgetObj, strContent):

        # 为当个组件设置内容
        # 支持按钮, 输入框

        if isinstance(widgetObj, wx.Button):
            widgetObj.SetLabel(strContent)
        else:
            widgetObj.SetValue(strContent)


    def saveContent(self):

        # 保存连接数据库弹框中填入的数据
        # 当有配置项发生更改时才会更新保存

        intIndex = 0
        dictHasChangeMsg = dict()
        dictGetSaveMsg = self.getContentFromWidgets()

        self.configParserObj.read(self.strConfigDirPath + self.strConfigFileName)

        for strKey, strValue in dictGetSaveMsg.items():

            strOldValue = self.configParserObj[self.configMsgObj.strConSessionName][strKey]
            if strOldValue != strValue:
                dictHasChangeMsg[strKey] = strValue
                intIndex = 1
            else:
                pass
        if intIndex == 1:
            self.logUtilObj.writerLog('[' + self.configMsgObj.strConSessionName + ']发生更改的配置项如下: ')
            for strHasChangeKey, strHasChangeValue in dictHasChangeMsg.items():
                self.logUtilObj.writerLog(strHasChangeKey + ': ' + strHasChangeValue)

            self.configureUtilObj.updateConfigSingleSession(self.configParserObj, self.configMsgObj.strConSessionName,
                                                            dictGetSaveMsg)
        else:
            pass


    def getContentFromWidgets(self):

        # 获取连接数据库中所有输入框中的内容, 存放到字典中返回

        dictGetSaveMsg = dict()
        dictGetSaveMsg[self.configMsgObj.strHostKey] = self.windowsObj.textCtrlIpObj.Value
        dictGetSaveMsg[self.configMsgObj.strPortKey] = self.windowsObj.textCtrlPortObj.Value
        dictGetSaveMsg[self.configMsgObj.strUserKey] = self.windowsObj.textCtrlUserNameObj.Value
        dictGetSaveMsg[self.configMsgObj.strPassWordKey] = self.windowsObj.textCtrlPasswdObj.Value

        # for strKey, strValue in dictGetSaveMsg.items():
        #
        #     self.logUtilObj.writerLog(strValue)
        #     if strValue == '':
        #         dictGetSaveMsg = None
        #         break

        return dictGetSaveMsg


    def checkWhetherNull(self, dictGetSaveMsg):

        # 检测输入是否完全

        intIndex = 1

        for strKey, strValue in dictGetSaveMsg.items():

            if strValue == '':

                intIndex = -1
                break
        return intIndex


    @staticmethod
    def getContentSingleWidget(widgetObj):

        # 获取单个组件的内容

        return widgetObj.Value


    def getContentForButtonTest(self):

        # 获取内容
        # 赋值给连接界面的弹框中的测试按钮

        if self.searchValuesObj.connectionMysqlObj is None:
            return '测试连接'
        else:
            return '断开连接'


    # def frameFocus(self, eventObj):
    #
    #     print('焦点..')
    #
    #     if self.searchValuesObj.connectionMysqlObj is None:
    #
    #
    #
    #         self.setContentSingleWidget(self.windowsObj.buttonTestConnectionObj, '测试连接')
    #     else:
    #         self.setContentSingleWidget(self.windowsObj.buttonTestConnectionObj, '断开连接')




