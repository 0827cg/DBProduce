#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: cg
# time  : 2018-07-11

import wx
from controll.setDialogControll import SetDialogControll

class SetDialog(wx.Dialog):

    # 设置界面弹框

    def __init__(self, parentObj, strTitle, intWidth=290, intHeight=210):
        super(SetDialog, self).__init__(parentObj, title=strTitle)

        self.setDialogControllObj = SetDialogControll(self, parentObj)

        # self.SetWindowStyle(style=(wx.MINIMIZE_BOX | wx.RESIZE_BORDER
        #                            | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX))
        self.SetSize(intWidth, intHeight)
        self.Center()

        self.__initUI()

        self.setDialogControllObj.setChoiceForComboBox()
        self.setDialogControllObj.setContent()

        # self.Show()
        self.ShowModal()




    def __initUI(self):

        # 初始化界面

        panelMasterObj = wx.Panel(self)
        panelMasterObj.SetBackgroundColour('#ffffff')

        boxSizerObj = wx.BoxSizer(wx.VERTICAL)
        panelMasterObj.SetSizer(boxSizerObj)

        boxSetObj = wx.BoxSizer(wx.HORIZONTAL)
        boxButtonObj = wx.BoxSizer(wx.HORIZONTAL)

        boxSizerObj.Add(boxSetObj, 2, flag=wx.ALL, border=5)
        boxSizerObj.Add(boxButtonObj, 0, flag=wx.ALL | wx.EXPAND, border=10)

        boxSetItemObj = wx.BoxSizer(wx.HORIZONTAL)
        boxSetMsgObj = wx.BoxSizer(wx.VERTICAL)

        # panelSetItemObj = wx.Panel(self)
        # panelSetItemObj.SetBackgroundColour('#ffffff')
        # panelSetItemObj.SetSizer(boxSetItemObj)

        # panelSetMsgObj = wx.Panel(self)
        # panelSetMsgObj.SetBackgroundColour('#ffffff')
        # panelSetMsgObj.SetSizer(boxSetMsgObj)

        # boxSetItemObj.Add(panelSetItemObj, 1, wx.EXPAND)
        # boxSetMsgObj.Add(panelSetMsgObj, 1, wx.EXPAND)

        boxSetObj.Add(boxSetItemObj, 0, flag=wx.ALL | wx.EXPAND, border=5)
        boxSetObj.Add(boxSetMsgObj, 0, flag=wx.ALL | wx.EXPAND, border=5)

        treeCtrlObj = wx.TreeCtrl(panelMasterObj, 1, wx.DefaultPosition, (60, 10), wx.TR_HIDE_ROOT | wx.TR_HAS_BUTTONS)
        # treeCtrlObj = wx.TreeCtrl(panelSetItemObj, 1, flag=wx.EXPAND | wx.TOP, border=0)
        treeRoot = treeCtrlObj.AddRoot('Setting')
        treeRootOutput = treeCtrlObj.AppendItem(treeRoot, '导出')
        #
        # treeCtrlObj.AppendItem(treeRootOutput, 'Linux')

        # staticTextHintObj = wx.StaticText(panelMasterObj, label='导出')
        boxSetItemObj.Add(treeCtrlObj, 0, flag=wx.TOP | wx.EXPAND, border=0)

        boxChooseSaveObj = wx.BoxSizer(wx.VERTICAL)

        boxSetMsgObj.Add(boxChooseSaveObj, 1, flag=wx.TOP | wx.EXPAND, border=0)


        boxPathObj = wx.BoxSizer(wx.HORIZONTAL)
        boxChoosePathObj = wx.BoxSizer(wx.HORIZONTAL)
        boxChooseTypeObj = wx.BoxSizer(wx.HORIZONTAL)

        boxChooseSaveObj.Add(boxPathObj, 0, flag=wx.TOP | wx.EXPAND, border=5)
        boxChooseSaveObj.Add(boxChoosePathObj, 0, flag=wx.TOP | wx.EXPAND, border=10)
        boxChooseSaveObj.Add(boxChooseTypeObj, 0, flag=wx.TOP | wx.EXPAND, border=15)

        labelHintSavePathObj = wx.StaticText(panelMasterObj, label='路  径:')
        self.textCtrlSavePathObj = wx.TextCtrl(panelMasterObj, size=(70, 23))

        boxPathObj.Add(labelHintSavePathObj, 0, flag=wx.TOP | wx.LEFT, border=2)
        boxPathObj.Add(self.textCtrlSavePathObj, 2, flag=wx.LEFT | wx.EXPAND, border=5)

        buttonSavePathObj = wx.Button(panelMasterObj, 205, label='选择文件夹', size=(75, 23))

        boxChoosePathObj.Add((1, 1), 2, wx.EXPAND, 0)
        boxChoosePathObj.Add(buttonSavePathObj, 0, flag=wx.ALIGN_RIGHT | wx.ALL, border=0)

        labelHintSaveNameObj = wx.StaticText(panelMasterObj, label='文件名: ')
        self.textCtrlSaveNameObj = wx.TextCtrl(panelMasterObj, size=(70, 23))

        self.comboBoxTypeObj = wx.ComboBox(panelMasterObj, -1, "类型", size=(70, 23))

        boxChooseTypeObj.Add(labelHintSaveNameObj, 0, flag=wx.TOP, border=2)
        boxChooseTypeObj.Add(self.textCtrlSaveNameObj, 0, flag=wx.RIGHT, border=0)
        boxChooseTypeObj.Add(self.comboBoxTypeObj, 0, flag=wx.LEFT, border=5)


        buttonConformObj = wx.Button(panelMasterObj, 206, label='确定', size=(38, 23))
        buttonConformObj.SetCursor(wx.Cursor(wx.CURSOR_HAND))

        buttonCancelObj = wx.Button(panelMasterObj, 207, label='取消', size=(38, 23))
        buttonCancelObj.SetCursor(wx.Cursor(wx.CURSOR_HAND))

        boxButtonObj.Add((1, 1), 2, wx.EXPAND, 0)
        boxButtonObj.Add(buttonConformObj, 0, flag=wx.RIGHT, border=10)
        boxButtonObj.Add(buttonCancelObj, 0, flag=wx.RIGHT, border=0)

        self.Bind(wx.EVT_BUTTON, self.setDialogControllObj.chooseButtonRun)


# if __name__ == '__main__':
#     app = wx.App()
#     setDialog = SetDialog(None, 'test')
#     app.MainLoop()