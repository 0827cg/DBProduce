#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: cg
# time  : 2018-07-26

import wx
from producebin.dbpObject import DBPObject
from producebin.utils.configMsg import ConfigMsg

class SetDialogControll(DBPObject):

    # 设置框的操作响应类

    def __init__(self, windowsObj, parentObj):

        self.windowsObj = windowsObj
        self.parentObj = parentObj
        self.configMsgObj = ConfigMsg()

        self.__listKey = [self.configMsgObj.strFilePathKey,
                          self.configMsgObj.strFileNameKey,
                          self.configMsgObj.strFileTypeKey]


    def chooseButtonRun(self, eventObj):

        # eventObj:  事件对象
        # 为所有界面中的按钮(button)赋予相对应的执行方法

        intId = eventObj.GetId()
        buttonObj = eventObj.GetEventObject()
        strChooseContent = buttonObj.GetLabel()
        self.logUtilObj.writerLog('press in ' + str(intId) + '-' + strChooseContent)

        if intId == 205:
            strPath = self.chooseDir()
            print(strPath)
            self.setContentSingle(self.windowsObj.textCtrlSavePathObj, strPath)
            # self.windowsObj.EndModal(intId)

        elif intId == 206:
            self.saveContent()
            self.windowsObj.EndModal(intId)

        elif intId == 207:
            self.windowsObj.EndModal(intId)


    def chooseDir(self):

        # 文件夹路径选择
        # 有选择(点击选择)则返回选择的文件夹路径, 无选择(点击取消)则返回None

        dirDialogObj = wx.DirDialog(self.parentObj, 'choose directory', style=wx.DD_DEFAULT_STYLE)
        try:
            if dirDialogObj.ShowModal() == wx.ID_OK:

                return dirDialogObj.GetPath()
            else:
                return None

        except:
            self.logUtilObj.writerLog('选择文件夹出错')

        finally:
            dirDialogObj.Destroy()


    def setContentSingle(self, widgetObj, strContent):

        # 为当个组件设置内容
        # widgetObj: 需要设置内容的组件对象
        # strContent: 需要设置的内容

        if strContent is not None:
            widgetObj.Value = strContent
        else:
            self.logUtilObj.writerLog('未发现内容')




    def setContent(self):

        # 为弹出框中的所有导出项设置内容
        # 其设置的内容是根据配置文件中的内容得到的

        intResult = self.configureUtilObj.checkConfigHasExist(self.configParserObj,
                                                              self.configMsgObj.strExportSessionName,
                                                              self.__listKey)
        if intResult == 1:

            dictConfig = self.configureUtilObj.getConfig(self.configParserObj)
            # self.setContentSingle(self.windowsObj.textCtrlSavePathObj, dictConfig[self.configMsgObj.strFilePathKey])
            self.windowsObj.textCtrlSavePathObj.SetValue(dictConfig[self.configMsgObj.strFilePathKey])
            self.windowsObj.textCtrlSaveNameObj.SetValue(dictConfig[self.configMsgObj.strFileNameKey])
            self.windowsObj.comboBoxTypeObj.SetValue(dictConfig[self.configMsgObj.strFileTypeKey])
        else:
            self.logUtilObj.writerLog('未找到相应的配置参数, intResult: ' + str(intResult))

    def saveContent(self):

        # 保存连接数据库弹框中填入的数据
        # 当有配置项发生更改时才会更新保存

        intIndex = 0
        dictHasChangeMsg = {}
        dictGetSaveMsg = self.getContentFromWidgets()

        self.configParserObj.read(self.strConfigDirPath + self.strConfigFileName)

        for strKey, strValue in dictGetSaveMsg.items():

            strOldValue = self.configParserObj[self.configMsgObj.strExportSessionName][strKey]
            if strOldValue != strValue:
                dictHasChangeMsg[strKey] = strValue
                intIndex = 1
            else:
                pass
        if intIndex == 1:
            self.logUtilObj.writerLog('[' + self.configMsgObj.strExportSessionName + ']发生更改的配置项如下: ')
            for strHasChangeKey, strHasChangeValue in dictHasChangeMsg.items():
                self.logUtilObj.writerLog(strHasChangeKey + ': ' + strHasChangeValue)

            self.configureUtilObj.updateConfigSingleSession(self.configParserObj,
                                                            self.configMsgObj.strExportSessionName, dictGetSaveMsg)

    def getContentFromWidgets(self):

        # 获取组件中输入的内容
        # 返回一个dict类型的

        dictGetSaveMsg = dict()
        dictGetSaveMsg[self.configMsgObj.strFilePathKey] = self.windowsObj.textCtrlSavePathObj.Value
        dictGetSaveMsg[self.configMsgObj.strFileNameKey] = self.windowsObj.textCtrlSaveNameObj.Value
        dictGetSaveMsg[self.configMsgObj.strFileTypeKey] = self.windowsObj.comboBoxTypeObj.Value

        return dictGetSaveMsg


    def setChoiceForComboBox(self):

        # 为下拉框设置可选的内容项

        listTypeName = ['md', 'html', 'text', 'word']
        self.windowsObj.comboBoxTypeObj.SetItems(listTypeName)

