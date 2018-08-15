#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: cg
# time  : 2018-08-15

import os
import base64

class CreateImagePy:

    # 独立类, 用来单独运行生成存放图片的base64值的py文件
    # 方式: CreateImagePy().generatePy(strImageTotalName)即可在同目录下生成一个和图片名字一样的py文件
    # 该py文件的使用方式, 先将其导入到需要使用的地方, 然后通过ImageBase().strBase64Content来获取该图片的base64值
    # 之后使用base64.b64decode(xxx)来编码并将其写入到缓存图片
    # 详情看produceFrame.py中的setFrameIcon()方法

    def __init__(self, strImageTotalName):

        # strImageTotalName: 图片文件路径

        self.strImageTotalName = strImageTotalName

    def generatePy(self):

        # 将base64内容写入到py文件(如存放则覆盖)
        # 并以ImageBase().strBase64Content来访问


        strTotalPyName = self.getImagePrefixName() + '.py'
        strBase64Content = self.getImageBase64()
        with open(strTotalPyName, 'w', encoding='utf-8') as fileObj:

            fileObj.write('#!/usr/bin/env python3\n')
            fileObj.write('# -*- coding: utf-8 -*-\n\n')

            fileObj.write('class ImageBase:\n')
            fileObj.write('\tdef __init__(self):\n')
            fileObj.write("\t\tself.strBase64Content = '")

        with open(strTotalPyName, 'ab+') as fileObj:
            fileObj.write(strBase64Content)


        with open(strTotalPyName, 'a', encoding='utf-8') as fileObj:
            fileObj.write("'")

    def getImagePrefixName(self):

        # 获取文件的前缀名

        if os.path.exists(self.strImageTotalName):

            strImageName = os.path.basename(self.strImageTotalName)
            strImagePrefixName = strImageName.split('.')[0]

            return strImagePrefixName
        else:
            return None

    def getImageBase64(self):

        # 获取图片base64值

        if os.path.exists(self.strImageTotalName):

            with open(self.strImageTotalName, 'rb') as fileObj:

                strBase64Content = base64.b64encode(fileObj.read())

            return strBase64Content
        else:
            return None



CreateImagePy('bitbug_favicon.ico').generatePy()



