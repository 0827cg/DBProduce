# -*- coding: utf-8 -*-

# author: cg错过
# time  : 2018-06-08

import wx
from win.produceFrame import DBFrame

class ProduceUI:

    # 界面入口

    def __init__(self, strTitle, intWidth, intHeight):

        self.app = wx.App()
        self.produceFrame = DBFrame(None, strTitle, intWidth, intHeight)
        self.app.MainLoop()
