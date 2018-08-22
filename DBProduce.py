# -*- coding: utf-8 -*-

# author: cg错过
# time  : 2018-06-08

import sys
from producebin.operatebin import OperateBin
from producebin.operateCheck import OperateCheck

def main():

    if OperateCheck().checkModuleExists() != 1:
        sys.exit(0)
    else:
        OperateBin()


if __name__ == '__main__':
    main()


