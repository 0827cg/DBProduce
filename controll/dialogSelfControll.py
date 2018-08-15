#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: cg
# time  : 2018-07-05

import sys
import time
from producebin.dbpObject import DBPObject


class DialogSelfControll(DBPObject):

    # 定义消息框执行的方法

    def __init__(self, windowsObj, parentObj):

        self.windowsObj = windowsObj
        self.parentObj = parentObj


    def chooseButtonRun(self, eventObj):

        # eventObj:  事件对象
        # 为所有界面中的按钮(button)赋予相对应的执行方法
        # 其中在退出按钮中(302), 需要先退出循环读取, 再停止线程, 最后关闭界面
        # # 这里再添加断开数据库连接--add time: 2018-08-09

        intId = eventObj.GetId()
        buttonObj = eventObj.GetEventObject()
        strChooseContent = buttonObj.GetLabel()
        self.logUtilObj.writerLog('press in ' + str(intId) + '-' + strChooseContent)

        if intId == 301:
            self.windowsObj.EndModal(intId)

        elif intId == 302:

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
            except:

                self.logUtilObj.writerLog('线程关闭出错, 程序可能卡死(建议杀死该进程)')
            else:

                self.windowsObj.EndModal(intId)
                time.sleep(0.3)

            finally:

                if self.parentObj.proFrameControllObj.searchValuesObj.connectionMysqlObj is not None:
                    self.parentObj.proFrameControllObj.searchValuesObj.connectionMysqlObj.close()
                    self.logUtilObj.writerLog('数据库连接已关闭')

                self.logUtilObj.writerLog('程序退出')


                sys.exit(0)

        elif intId == 303:
            self.windowsObj.EndModal(intId)

        else:
            self.logUtilObj.writerLog('press in ' + str(intId) + '-未给id= ' + str(intId) + '的按钮组件分配方法')