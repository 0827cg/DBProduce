#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: cg
# time  : 2018-09-14

import time
import datetime


class TimeUtil:

    # 时间类

    @staticmethod
    def getTime(strFormat):

        # 按照格式获取时间
        # strFormat: 时间格式

        nowTime = time.localtime()
        strFormatTime = time.strftime(strFormat, nowTime)
        return strFormatTime

    def getDateTime(self):
        return self.getTime("%Y-%m-%d %H:%M:%S")

    def getNumSecondTime(self):
        return self.getTime("%Y%m%d%H%M%S")

    def getNumHourTime(self):
        return self.getTime("%Y%m%d%H")

    def getNumDayTime(self):
        return self.getTime("%Y%m%d")

    def getMinTime(self):
        return self.getTime("%M")

    def getHourTime(self):
        return self.getTime("%H")

    def getHourMinTime(self):
        return self.getTime("%H%M")

    @staticmethod
    def getPastDataDay(intDayNum):

        # 根据天数，来获取过去距离今天intDayNum天的日期
        # intDayNum: int类型, 表示天数
        # 返回的是一个date对象类型的日期,格式是"%Y-%m-%d"

        strToday = datetime.date.today()

        # strToday的日期格式就是"%Y-%m-%d"
        strOtherday = strToday - datetime.timedelta(days=intDayNum)

        return strOtherday

    @staticmethod
    def getFutureDataDay(intDayNum):

        # 根据天数，来获取未来距离今天intDayNum天的日期
        # intDayNum: int类型, 表示天数
        # 返回的是一个date对象类型的日期,格式是"%Y-%m-%d"

        strToday = datetime.date.today()

        # strToday的日期格式就是"%Y-%m-%d"
        strOtherday = strToday + datetime.timedelta(days=intDayNum)

        return strOtherday

    @staticmethod
    def getTimeStamp(strDate, strFormatDate):

        # 根据日期，获取时间戳
        # strDate: 字符串类型的日期
        # strFormatDate: 与strDate先对应的日期格式，例如"%Y-%m-%d"
        # 返回一个int类型的时间戳

        timeArray = time.strptime(strDate, strFormatDate)
        timeStamp = time.mktime(timeArray)

        return int(timeStamp)

    @staticmethod
    def getTodayStamp():

        # 获取今天的时间戳
        # 返回的是一个int类型的时间戳,日期格式是"%Y-%m-%d"

        strToday = datetime.date.today()
        timeArray = time.strptime(str(strToday), "%Y-%m-%d")
        timeStamp = time.mktime(timeArray)

        return int(timeStamp)

    @staticmethod
    def getDateByStamp(intStamp):

        # 根据时间戳获取日期时间
        # intStamp: 十位/十三位时间戳, int类型
        # 日期时间格式: "%Y-%m-%d %H:%M:%S"

        if len(str(intStamp)) > 10:
            intNewStamp = int(round(intStamp/1000))
        else:
            intNewStamp = intStamp

        structTimeDate = time.localtime(intNewStamp)
        return time.strftime("%Y-%m-%d %H:%M:%S", structTimeDate)

