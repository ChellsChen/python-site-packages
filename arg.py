#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date       : 2015-06-09 16:07:14
# Author     : 陈小雪
# E-mail     : shell_chen@yeah.net
# Version    : 1.0.1

import os
import time
import argparse
import os


parser = argparse.ArgumentParser()

parser.add_argument("-f", help="publish article filename", required = True)
parser.add_argument("-path", help = "publish to path", default = os.getcwd())
parser.add_argument("-t", help = "article title", default = int(time.time()))
parser.add_argument("-c", help="article class", default="未分类")
parser.add_argument("-tags", help="article tags",default="其他")

args = parser.parse_args()




