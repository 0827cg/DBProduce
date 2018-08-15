#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: cg
# time  : 2018-08-14

from producebin.dbpObject import DBPObject


class CheckEnv(DBPObject):

    # 模块检测


    def checkEnv(self, arrModuleName):

        # 检测本地系统中所需要的环境是否完全

        try:

            # map(__import__, arrModuleName)

            for arrItem in arrModuleName:
                self.__checkModule(arrItem)

        except ImportError:
            self.logUtilObj.writerLog('检测到系统中有模块未安装')
            intIndex = -1
            return intIndex

        else:
            return 1


    def __checkModule(self, strModuleName):

        # 检测模块是否安装

        try:

            map(__import__, strModuleName)

        except ImportError:
            self.logUtilObj.writerLog('检测到系统中未安装' + strModuleName + '模块')
            intIndex = -1
            return intIndex

        else:
            self.logUtilObj.writerLog('检测到系统中已经安装' + strModuleName + '模块')
            return 1


