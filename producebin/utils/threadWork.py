#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: cg
# time  : 2018-07-10

import wx
import threading
from producebin.dbpObject import DBPObject

class ThreadWork(threading.Thread, DBPObject):

    '''
    自定义线程, 目的为读取并渲染日志内容到界面
    '''

    def __init__(self, parentObj):

        threading.Thread.__init__(self)
        self.parentObj = parentObj
        self.eventMarkObj = threading.Event()
        self.eventMarkObj.clear()

    def stop(self):
        self.eventMarkObj.set()


    def run(self):

        # strLastContent = self.parentObj.proFrameControllObj.getLogMsg()
        # timeRead = os.stat(self.logUtilObj.strLogFileName).st_mtime
        # 1531191892.5658703
        # timeTest = os.stat(self.logUtilObj.strLogFileName).st_mtime_ns
        # 1531191892565870400

        while True:

            if self.eventMarkObj.isSet():
                self.logUtilObj.writerLog('threading event is set, 线程将退出')
                break
            else:

                fieldContent = self.contentUtilObj.getTailLog()
                for strContent in fieldContent:

                    wx.CallAfter(self.parentObj.proFrameControllObj.setLogMsgWinShow, strContent)
                    # time.sleep(1)



