#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import argparse

curdir = os.path.dirname(os.path.realpath(__file__))

def remove_file(path):
    _dir, ext = os.path.splitext(path)
    if ext == '.pyc':
        print 'remove : %s'%path
        os.remove(path)

def parse_path(path):
    args = os.path.abspath(path)
    if os.path.isfile(path):
        remove_file(path)

    for root, dirs, names in os.walk(path):
        for name in names:
            file_path = os.path.join(root, name)
            remove_file(file_path)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        args = sys.argv[1]
    else:
        args = curdir
    parse_path(args)



