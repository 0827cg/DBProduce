## DBProduce

简单的数据库字典生成工具, 使用python3编写, 用的GUI是wxpython

程序运行截屏:

<div align=center>
	<img src='https://github.com/cgstudios/DBProduce/blob/master/img/img-win-readme.png'/>
</div>

用到的模块

* pymysql
* wx

即运行环境需要这些, 模块安装完成之后使用命令`python DBProduce.py`来运行

当然我也打包了[exe下载][0]

### 描述

目前仅支持导出`markdown`格式文档, 后续可以支持多种文档, 先已经提供导出的模块类型引入选择, 如需要新增模块类, 其该类中需要包含
一个静态方法, 方法名为`showFileType`, 方法内容就是返回导出类型的名字,如定义一个导出`markdown`格式的类
```
class XXX(DBProduce):

    ...
    @staticmethod
    def showFileType():

        return 'md'
```

之后需要在`producebin/module/__init__.py`中进行引入

> author: cg错过

> create Time: 2018-06-08

> first commit time: 2018-08-15


[0]: https://github.com/cgstudios/DBProduce/releases/tag/1.0.0


