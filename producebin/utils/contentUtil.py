#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: cg
# time  : 2018-08-03

import os

class ContentUtil:

    booleanGetTailExit = False

    def __init__(self, strFileName):
        self.strFileName = strFileName

    def getTailLog(self):

        # 实现的功能类似tail -f命令读取日志内容
        # add in 2018-08-03
        # 返回迭代器

        with open(self.strFileName, 'rb') as fileObj:
            pos = fileObj.seek(0, os.SEEK_END)

            try:

                while True:

                    if self.booleanGetTailExit:
                        break

                    # currentPos = fileObj.seek(0, os.SEEK_END)
                    # print(pos)
                    #
                    # if currentPos > pos:
                    #     pos = fileObj.seek(0, os.SEEK_END)
                    #     continue

                    strLineContent = fileObj.readline()
                    if not strLineContent:
                        continue
                    else:
                        yield strLineContent.decode('utf-8').strip('\n')
            except KeyboardInterrupt:
                pass


    def setBooleanGetTailExit(self, boolean):
        self.booleanGetTailExit = boolean