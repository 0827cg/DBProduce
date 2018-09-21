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

        return '.md'
```

之后需要在`producebin/module/__init__.py`中进行引入, 然后在`producebin/util/exportType.py`中的`listClassName`集合中添加
元素, 元素即创建的类名

这样做的目的, 仅仅只是为了能读取到可供导出的类型的种类个数

### 不足

这里有个问题, 就是程序运行起来很耗内存, 内存占用`16%`.....这是个悲催的故事

所以, 这个并不是正式版, 还需要开发优化

***

> 注: 个人项目, 不定期维护更新

> author: cg错过

> create Time: 2018-06-08

> first commit time: 2018-08-15


[0]: https://github.com/0827cg/DBProduce/releases


