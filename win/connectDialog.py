#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: cg
# time  : 2018-07-04

import wx
from controll.connectDialogControll import ConnectDialogControll

class ConnectDialog(wx.Dialog):

    # 连接数据库界面弹框

    def __init__(self, parentObj, strTitle, intWidth, intHeight):
        super(ConnectDialog, self).__init__(parentObj, title=strTitle)

        self.connectDialogControll = ConnectDialogControll(self, parentObj)

        # self.SetWindowStyle(style=(wx.MINIMIZE_BOX | wx.RESIZE_BORDER
        #                            | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX))
        self.SetSize(intWidth, intHeight)
        self.Center()

        self.__initUI()

        self.connectDialogControll.setContent()

        # self.Show()
        self.ShowModal()


    def __initUI(self):

        # 初始化界面

        panelMasterObj = wx.Panel(self)
        panelMasterObj.SetBackgroundColour('#ffffff')

        boxSizerObj = wx.BoxSizer(wx.VERTICAL)
        panelMasterObj.SetSizer(boxSizerObj)

        boxInputObj = wx.BoxSizer(wx.VERTICAL)
        boxButtonObj = wx.BoxSizer(wx.HORIZONTAL)

        boxSizerObj.Add(boxInputObj, 2, flag=wx.ALL, border=5)
        boxSizerObj.Add(boxButtonObj, 0, flag=wx.ALL | wx.EXPAND, border=5)

        boxIpObj = wx.BoxSizer(wx.HORIZONTAL)
        boxPortObj = wx.BoxSizer(wx.HORIZONTAL)
        boxUserNameObj = wx.BoxSizer(wx.HORIZONTAL)
        boxPasswdObj = wx.BoxSizer(wx.HORIZONTAL)

        boxInputObj.Add(boxIpObj, 0, flag=wx.TOP | wx.EXPAND, border=15)
        boxInputObj.Add(boxPortObj, 0, flag=wx.TOP | wx.EXPAND, border=10)
        boxInputObj.Add(boxUserNameObj, 0, flag=wx.TOP | wx.EXPAND, border=10)
        boxInputObj.Add(boxPasswdObj, 0, flag=wx.TOP | wx.EXPAND, border=10)

        staticIpObj = wx.StaticText(panelMasterObj, label='ip地址:')
        self.textCtrlIpObj = wx.TextCtrl(panelMasterObj, 201, size=(120, 22))
        boxIpObj.Add(staticIpObj, 0, flag=wx.LEFT, border=10)
        boxIpObj.Add(self.textCtrlIpObj, 0, flag=wx.LEFT, border=16)

        staticPortObj = wx.StaticText(panelMasterObj, label='端口号:')
        self.textCtrlPortObj = wx.TextCtrl(panelMasterObj, 202, size=(120, 22))
        boxPortObj.Add(staticPortObj, 0, flag=wx.LEFT, border=10)
        boxPortObj.Add(self.textCtrlPortObj, 0, flag=wx.LEFT, border=15)

        staticUserNameObj = wx.StaticText(panelMasterObj, label='用户名:')
        self.textCtrlUserNameObj = wx.TextCtrl(panelMasterObj, 203, size=(120, 22))
        boxUserNameObj.Add(staticUserNameObj, 0, flag=wx.LEFT, border=10)
        boxUserNameObj.Add(self.textCtrlUserNameObj, 0, flag=wx.LEFT, border=15)

        staticPasswdObj = wx.StaticText(panelMasterObj, label='密码:')
        self.textCtrlPasswdObj = wx.TextCtrl(panelMasterObj, 204, size=(120, 22))
        boxPasswdObj.Add(staticPasswdObj, 0, flag=wx.LEFT, border=10)
        boxPasswdObj.Add(self.textCtrlPasswdObj, 0, flag=wx.LEFT, border=27)

        strContent = self.connectDialogControll.getContentForButtonTest()
        self.buttonTestConnectionObj = wx.Button(panelMasterObj, 205, label=strContent, size=(70, 23))
        self.buttonTestConnectionObj.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        self.buttonTestConnectionObj.SetBackgroundColour('#efefef')


        self.buttonConformObj = wx.Button(panelMasterObj, 206, label='确定', size=(38, 23))
        self.buttonConformObj.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        if '断开' in strContent:
            # self.buttonConformObj.Disable()
            self.buttonConformObj.Enable(False)
        else:
            self.buttonConformObj.Enable()

        buttonCancelObj = wx.Button(panelMasterObj, 207, label='取消', size=(38, 23))
        buttonCancelObj.SetCursor(wx.Cursor(wx.CURSOR_HAND))

        boxButtonObj.Add(self.buttonTestConnectionObj, 0, flag=wx.LEFT | wx.BOTTOM, border=10)
        boxButtonObj.Add(self.buttonConformObj, 0, flag=wx.LEFT, border=29)
        boxButtonObj.Add(buttonCancelObj, 0, flag=wx.ALIGN_RIGHT)

        self.Bind(wx.EVT_BUTTON, self.connectDialogControll.chooseButtonRun)
        # self.Bind(wx.EVT_SET_CURSOR, self.connectDialogControll.frameFocus)

