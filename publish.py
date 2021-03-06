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
# import arg
import logging
import time

class BlogData(object):
    def __init__(self, path):
        self.path = path
        self.indexfile = os.path.join(path, "index.json")
        self.classflie = os.path.join(path, "class.json")
        self.tagsfile = os.path.join(path, "tags.json")
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
        tmp = None
        if os.path.isfile(filename):
            try:
                tmp = json.load(open(filename))
            except:
                tmp = None
                print "load pickle:%s error!" %filename
        return tmp

    def _dumps(self, obj, filename):
        d = json.dumps(obj, sort_keys=True, indent=4)
        with open(filename,"w") as fp:
            fp.write(d)


    def add(self,title, context, tags, cls, public=0):
        Id = self.getid()
        mtime = ctime = time.time()
        info = [title, tags, cls, ctime, mtime, public]

        self.setinfo(Id, context,info)

    def update(self, Id, title, context, tags, cls, public):
        mtime = time.time()
        info = self._INDEX.get(Id)
        if info is None:
            return

        ctime = info[3]
        self.setinfo(Id, context, [title, tags, cls, ctime, mtime, public])

    def setinfo(self, Id, context, info):

        dirpath = os.path.join(self.path, str(Id))
        if os.path.isdir(dirpath):
            logging.error("%s dupile"%dirpath)
            return

        if not self.write(Id, context):
            return

        self.tagsadd(info[1])
        self.clsadd(Id, info[2])
        self.indexadd(Id,info)
        self.dumps()

    def write(self, Id, context):
        dirpath = os.path.join(self.path, str(Id))

        if not os.path.isdir(dirpath):
            try:
                os.mkdir(dirpath)
            except:
                logging.exception("mkdir %s fail"%dirpath)
                return False

        fpdir = os.path.join(dirpath, "index.html")
        with open(fpdir, "w") as fp:
            fp.write(context)

        fpdir = os.path.join(dirpath, "index.md")
        with open(fpdir, "w") as fp:
            fp.write(context)

        return True

    def tagsadd(self, tags):
        if self._TAGS is None:
            self._TAGS = [ ]

        for t in tags:
            if t not in self._TAGS:
                self._TAGS.append(t)

    def clsadd(self, Id, cls):
        if not self._CLASS:
            self._CLASS = { }

        c = self._CLASS.get(cls)
        if not c:
            self._CLASS[cls] = [Id]
        else:
            c.append(Id)

    def indexadd(self, Id, info):
        if not self._INDEX:
            self._INDEX = { }
        self._INDEX[Id] = info



# def test():
#     args = arg.args

if __name__ == "__main__":
    bd = BlogData("/home/cxx/shell/blog/store")
    bd.add('bbcc', "bbbbbbbccc",["bbb"],"bbb")


