#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date       : 2015-06-09 15:21:13
# Author     : 陈小雪
# E-mail     : shell_chen@yeah.net
# Version    : 1.0.1
"""
发布流程:
1. 运行pulish.py脚本,
    参数 -f:filename
         -tags:tags
         -title:tile
         -p: dirpath
         -c: fileclass

2. 初始化待发布文章信息:
    id : 文章id
    title :文章标题
    tags : 文章标签
    class : 文章所属类别
    publishtime: 发布时间
    dirpath : 发布的路径

3. 加载json文件
    tagsfile: 标签下对应的文件
    classfile:  分类文章
    indexfile:  文章信息

4. 发布过程
    将file.md转换成file.html文件
    copy file.html文件到发布路径所在目录
    将待发布文章信息保存到各json对象中

"""

import os
import json
import arg

class Publish(object):
    indexfile = "index.json"
    classflie = "class.json"
    tagsfile = "tags.json"

    def __init__(self, filename, title, tags, cls, path):
        self.id = self.getid()
        self.filename = filename
        self.title = title
        self.tags = tags
        self.cls = cls
        self.path = path
        self.loads()

    def getid(self):
        return int(time.time() - 1419598800)

    def loads(self):
        self._INDEX = self._loads(self.indexfile)
        self._CLASS = self._loads(self.classflie)
        self._TAGS = self._loads(self.tagsfile)

    def dumps(self):
        self._dumps(self._INDEX, self.indexfile)
        self._dumps(self._CLASS, self.classflie)
        self._dumps(self._TAGS, self.tagsfile)

    def _loads(self, filename):
        tmp = [ ]
        filedir = os.path.join(self.path, filename)
        if os.path.isfile(filedir):
            try:
                tmp = json.load(open(filename))
                print "load pickle:%s" %filename
            except:
                tmp = [ ]
                print "load pickle:%s error!" %filename
        return tmp

    def _dumps(self, obj, filename):
        json.dump(obj, open(filename, "w"), sort_keys=True, indent=4)





def start():
    args = arg.args

if __name__ == "__main__":
    start()


