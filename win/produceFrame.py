#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: cg
# time  : 2018-07-04


import wx
import os
import base64
from controll.proFrameControll import ProFrameControll
from producebin.dbpObject import DBPObject
from producebin.utils.icon import ImageBase

class DBFrame(wx.Frame, DBPObject):

    strTotalContent = ''
    listThread = []
    # listFileType = []
    # intCursor = 0

    def __init__(self, parentObj, strTitle, intWidth, intHeight):
        super(DBFrame, self).__init__(parentObj, title=strTitle)


        self.proFrameControllObj = ProFrameControll(self)

        self.listFileType = self.proFrameControllObj.getFileTypeToExport()

        self.SetWindowStyle(style=(wx.SIMPLE_BORDER | wx.CAPTION | wx.MINIMIZE_BOX | wx.CLOSE_BOX ))
        # self.SetWindowStyle(style=(wx.MINIMIZE_BOX | wx.RESIZE_BORDER
        #                            | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.SIMPLE_BORDER))
        self.SetSize(intWidth, intHeight)
        self.Center()



        self.__initUI()

        self.Show()

        self.proFrameControllObj.startThreadForLog()


    def __initUI(self):

        # 初始化主界面

        menuBarObj = wx.MenuBar()

        chooseMenuObj = wx.Menu()
        aboutMenuObj = wx.Menu()

        menuBarObj.Append(chooseMenuObj, '选项')
        menuBarObj.Append(aboutMenuObj, '关于')

        self.SetMenuBar(menuBarObj)

        connectionMenuItemObj = wx.MenuItem(None, 101, '连接')
        setMenuItemObj = wx.MenuItem(None, 102, '设置')
        exitMenuItemObj = wx.MenuItem(chooseMenuObj, wx.ID_EXIT, '退出')
        chooseMenuObj.Append(connectionMenuItemObj)
        chooseMenuObj.Append(setMenuItemObj)
        chooseMenuObj.Append(exitMenuItemObj)

        aboutMenuItemObj = wx.MenuItem(aboutMenuObj, 103, '关于工具')
        aboutMenuObj.Append(aboutMenuItemObj)

        panelMasterObj = wx.Panel(self)
        panelMasterObj.SetBackgroundColour('#ffffff')

        boxSizerObj = wx.BoxSizer(wx.VERTICAL)
        panelMasterObj.SetSizer(boxSizerObj)

        boxShowListObj = wx.BoxSizer(wx.HORIZONTAL)
        boxShowLogObj = wx.BoxSizer(wx.VERTICAL)

        boxSizerObj.Add(boxShowListObj, 2, flag=wx.ALL, border=5)
        boxSizerObj.Add(boxShowLogObj, 1, flag=wx.ALL | wx.EXPAND, border=5)

        self.checkListBoxObj = wx.CheckListBox(panelMasterObj, style=0, name='ChecklistBox')
        boxShowListObj.Add(self.checkListBoxObj, 2, flag=wx.ALL | wx.EXPAND, border=5)

        boxChooseAndConformObj = wx.BoxSizer(wx.VERTICAL)

        boxShowListObj.Add(boxChooseAndConformObj, 1, flag=wx.ALL | wx.EXPAND | wx.RIGHT, border=0)

        boxComboBoxObj = wx.BoxSizer(wx.HORIZONTAL)
        boxChooseObj = wx.BoxSizer(wx.HORIZONTAL)
        boxConformObj = wx.BoxSizer(wx.VERTICAL)

        boxChooseAndConformObj.Add(boxComboBoxObj, 0, flag=wx.ALL | wx.EXPAND, border=5)
        boxChooseAndConformObj.Add(boxChooseObj, 2, flag=wx.ALL | wx.TOP | wx.EXPAND, border=5)
        boxChooseAndConformObj.Add(boxConformObj, 0, flag=wx.EXPAND, border=0)

        self.radioButtonObj = wx.RadioButton(panelMasterObj, 104, '全选')
        self.radioButtonNoObj = wx.RadioButton(panelMasterObj, 105, '反选')
        self.radioButtonNoObj.SetValue(True)

        self.comboBoxObj = wx.ComboBox(panelMasterObj, 106, '选择数据库')

        boxComboBoxObj.Add(self.comboBoxObj, 0, flag=wx.TOP, border=0)

        boxChooseObj.Add(self.radioButtonObj, 0, flag=wx.TOP, border=5)

        boxChooseObj.Add(self.radioButtonNoObj, 0, flag=wx.TOP, border=5)

        buttonConformObj = wx.Button(panelMasterObj, 107, label='确认导出', size=(96, 26))
        buttonConformObj.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        boxConformObj.Add(buttonConformObj, 1, flag= wx.BOTTOM | wx.LEFT, border=5)

        self.textCtrlLogShowObj = wx.TextCtrl(panelMasterObj, style=wx.TE_MULTILINE|wx.TE_RICH2)
        intPointSize = self.textCtrlLogShowObj.GetFont().GetPointSize()
        newFontObj = wx.Font(intPointSize - 1, wx.DEFAULT, wx.NORMAL, wx.LIGHT, underline=False)
        self.textCtrlLogShowObj.SetFont(newFontObj)
        self.textCtrlLogShowObj.SetBackgroundColour('#2e2e2e')
        self.textCtrlLogShowObj.SetForegroundColour('#cccccc')

        boxShowLogObj.Add(self.textCtrlLogShowObj, 2, flag= wx.BOTTOM | wx.LEFT | wx.RIGHT | wx.EXPAND, border=5)

        # panelTail = wx.Panel(panelMasterObj)
        panelTail = wx.Panel(panelMasterObj, size=(320, 19))
        panelTail.SetBackgroundColour('#efefef')
        staticTextHintObj = wx.StaticText(panelTail, label='v1.0.0', size=(45, 15), pos=(260, 2))
        # boxSizerObj.Add(staticTextHintObj, 0, flag=wx.ALIGN_RIGHT | wx.BOTTOM, border=3)

        boxSizerObj.Add(panelTail, 0, flag=wx.ALL | wx.EXPAND, border=0)


        # 若用如下方式设置窗口图标, 那么在打包exe时并不会将ico图标打包进exe
        # iconObj = wx.Icon()
        # iconObj.CopyFromBitmap(wx.Bitmap("DBProduce.ico", type=wx.BITMAP_TYPE_ICO))
        # self.SetIcon(iconObj)

        # 采用此方式设置, 这样打包不受影响
        self.__setFrameIcon('DBProduce_frame.ico')

        self.Bind(wx.EVT_MENU, self.proFrameControllObj.chooseMenuRun)
        self.Bind(wx.EVT_RADIOBUTTON, self.proFrameControllObj.chooseRadioButton)
        self.Bind(wx.EVT_COMBOBOX, self.proFrameControllObj.comboboxEvent)
        self.Bind(wx.EVT_COMBOBOX_CLOSEUP, self.proFrameControllObj.comboboxCloseUp)
        self.Bind(wx.EVT_BUTTON, self.proFrameControllObj.chooseButtonRun)
        self.Bind(wx.EVT_CLOSE, self.proFrameControllObj.closeWin)
        self.Bind(wx.EVT_SET_CURSOR, self.proFrameControllObj.frameFocus)


    def __setFrameIcon(self, strIconName):

        # 设置图标
        # 这里的图标是从代码文件中读取而来
        # utils.icon.py文件中的变量strBase64Content存放这图标文件的base64值
        # 这里做的只是将strBase64Content的值读取出来, 写到一个缓存图片中, 将这个缓存图片设置到窗口图标
        # 这个utils/icon.py的文件是用
        # 这样就可以理解为将图标打包进exe

        with open(strIconName, 'wb') as fileObj:

            fileObj.write(base64.b64decode(ImageBase().strBase64Content))

        iconObj = wx.Icon()
        iconObj.CopyFromBitmap(wx.Bitmap(strIconName, type=wx.BITMAP_TYPE_ICO))
        self.SetIcon(iconObj)
        os.remove(strIconName)
