#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: cg
# time  : 2018-07-05

import wx
from controll.dialogSelfControll import DialogSelfControll


class DialogSelf(wx.Dialog):

    def __init__(self, parentObj, strTitle, strContent, intWidth=210, intHeight=111):
        super(DialogSelf, self).__init__(parentObj, title=strTitle)

        self.strContent = strContent
        self.dialogSelfControllObj = DialogSelfControll(self, parentObj)

        # self.SetWindowStyle(style=(wx.MINIMIZE_BOX | wx.RESIZE_BORDER
        #                            | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX))
        self.SetSize(intWidth, intHeight)
        self.Center()


    def showMessageUI(self):

        # 消息显示框

        panelMasterObj = wx.Panel(self)
        panelMasterObj.SetBackgroundColour('#ffffff')

        boxSizerObj = wx.BoxSizer(wx.VERTICAL)
        panelMasterObj.SetSizer(boxSizerObj)

        boxShowMsgObj = wx.BoxSizer(wx.VERTICAL)
        boxButtonObj = wx.BoxSizer(wx.VERTICAL)

        boxSizerObj.Add(boxShowMsgObj, 0, flag=wx.TOP | wx.EXPAND, border=5)
        boxSizerObj.Add(boxButtonObj, 0, flag=wx.TOP | wx.EXPAND, border=6)

        # staticCtrlMsgObj = wx.StaticText(panelMasterObj, label=self.strContent, style=wx.ALIGN_CENTER)
        staticCtrlMsgObj = wx.StaticText(panelMasterObj, label=self.strContent)

        boxShowMsgObj.Add(staticCtrlMsgObj, 1, flag=wx.ALL | wx.EXPAND, border=5)

        buttonConformObj = wx.Button(panelMasterObj, 301, label='确定', size=(40, 23))

        boxButtonObj.Add(buttonConformObj, 0, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)

        self.Bind(wx.EVT_BUTTON, self.dialogSelfControllObj.chooseButtonRun)

        self.ShowModal()


    def showChooseUI(self):

        # 消息选择框

        panelMasterObj = wx.Panel(self)
        panelMasterObj.SetBackgroundColour('#ffffff')

        boxSizerObj = wx.BoxSizer(wx.VERTICAL)
        panelMasterObj.SetSizer(boxSizerObj)

        boxShowMsgObj = wx.BoxSizer(wx.VERTICAL)
        boxButtonObj = wx.BoxSizer(wx.HORIZONTAL)

        boxSizerObj.Add(boxShowMsgObj, 0, flag=wx.TOP | wx.EXPAND, border=5)
        boxSizerObj.Add(boxButtonObj, 0, flag=wx.TOP | wx.EXPAND, border=7)

        # staticCtrlMsgObj = wx.StaticText(panelMasterObj, label=self.strContent, style=wx.ALIGN_CENTER)
        staticCtrlMsgObj = wx.StaticText(panelMasterObj, label=self.strContent)

        boxShowMsgObj.Add(staticCtrlMsgObj, 1, flag=wx.ALL | wx.EXPAND, border=5)

        buttonConformObj = wx.Button(panelMasterObj, 302, label='确定', size=(40, 23))
        buttonCancelObj = wx.Button(panelMasterObj, 303, label='取消', size=(40, 23))

        intCurrentWidth = wx.Size(self.GetSize()).GetWidth()

        boxButtonObj.Add(buttonConformObj, 0, flag=wx.LEFT, border=(intCurrentWidth / 2 - 10))
        boxButtonObj.Add(buttonCancelObj, 0, flag=wx.LEFT, border=8)
        # print(wx.Size(self.GetSize()).GetWidth())

        self.Bind(wx.EVT_BUTTON, self.dialogSelfControllObj.chooseButtonRun)

        self.ShowModal()




# if __name__ == '__main__':
#     app = wx.App()
#     dialogSelfObj = DialogSelf(None, 'test', ' test')
#     dialogSelfObj.showMessageUI()
#     app.MainLoop()