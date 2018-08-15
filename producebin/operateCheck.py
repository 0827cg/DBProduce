#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: cg
# time  : 2018-08-14

from producebin.dbpObject import DBPObject
from producebin.utils.checkEnv import CheckEnv


class OperateCheck(DBPObject):

    # 检测执行需要用到的模块是否安装
    # 如后期需要添加模块, 则在此处添加到arrModuleName中

    arrModuleName = list()
    arrModuleName.append('wx')
    arrModuleName.append('pymysql')


    def checkModuleExists(self):

        # 检测模块是否存在

        checkEnvObj = CheckEnv()
        intResult = checkEnvObj.checkEnv(self.arrModuleName)

        if intResult != 1:
            self.logUtilObj.writerLog('执行环境不足, 程序退出')
            return -1
        else:
            self.logUtilObj.writerLog('执行环境完全, 将选择启动程序')
            return 1


