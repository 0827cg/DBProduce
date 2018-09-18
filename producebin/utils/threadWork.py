#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: cg
# time  : 2018-07-10

import wx
import threading
from producebin.dbpObject import DBPObject

class ThreadLog(threading.Thread, DBPObject):

    '''
    自定义线程, 目的为读取并渲染日志内容到界面
    '''

    # 今天着手处理一个问题, 就是读取日志渲染到主界面中出现延时致卡死的问题
    # 其实这个问题早在开发的时候就发现了, 也就是点击导出按钮之后, 渲染界面显示日志出现延时
    # 开始我以为是实现的tail功能的方法问题, 后面琢磨测试了发现不是tail的问题, 而是子线程通知主线程渲染的时候的问题
    # 该情景是, 点击导出按钮, 程序主线程执行导出功能, 然而子线程中代码wx.CallAfter()方法将内容通知主线程渲染显示到界面, 主线程需要先将
    # 导出的事物执行完成之后, 再执行wx.CallAfter()方法返回来的需要执行的事物, 所以此时出现了延时
    # 目前还未解决--add in 2018-09-17 16:51

    # 接上问题已解决
    # 针对上面的问题, 目前我的解决方式是新增一条子线程, 导出模块丢给子线程执行,例如下面我新增的ThreadExport类
    # 这样实现的结果是上面的问题将得到解决, 即不会产生延时, 但主线程交替调用子线程导致了耗时增多,导出耗时较以前主线程导出多了一倍时间
    # add in 2018-09-18 15:18

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
                self.logUtilObj.writerLog('ThreadLog event is set, 子线程退出')
                break
            else:

                fieldContent = self.contentUtilObj.getTailLog()
                for strContent in fieldContent:

                    # self.parentObj.proFrameControllObj.setLogMsgWinShow(strContent)
                    wx.CallAfter(self.parentObj.proFrameControllObj.setLogMsgWinShow, strContent)
                    # time.sleep(1)


class ThreadExport(threading.Thread, DBPObject):

    # 导出模块的子线程
    # 启动线程即执行导出, 执行导出之后将自动停止线程
    # add in 2018-09-18 10

    def __init__(self, func, args):

        # func: 接受一个方法(python3已规定此参数)
        # args: 接受一个参数, 该参数为传递给func方法使用

        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        # self.parentObj = parentObj
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
                self.logUtilObj.writerLog('ThreadExport event is set, 子线程退出')
                break
            else:
                self.func(self.args)
                self.eventMarkObj.set()








