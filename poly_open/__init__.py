'''
This software is released under an MIT/X11 open source license.

Copyright 2013-2014 Diffeo, Inc.
'''

import __builtin__
import os
import pydoop.hdfs as hdfs
import shutils

## see more info on HDFS here: http://pydoop.sourceforge.net/docs/tutorial/hdfs_api.html

def _poly_open(path, *args, **kwargs):
    if path.startswith('hdfs:'):
        return hdfs.open(path, *args, **kwargs)
    else:
        return open(path, *args, **kwargs)

__builtin__.open = _poly_open


def _poly_ls(path, *args, **kwargs):
    if path.startswith('hdfs:'):
        return hdfs.ls(path, *args, **kwargs)
    else:
        return os.listdir(path)

os.listdir = _poly_ls


def _poly_rename(path, *args, **kwargs):
    if path.startswith('hdfs:'):
        if not args[1].startswith('hdfs:'):
            raise Exception('poly_open.rename(hdfs, non-hdfs) not implemented')
        return hdfs.move(path, *args, **kwargs)
    else:
        return os.listdir(path)

os.rename = _poly_rename


def _poly_mkdir(path, *args, **kwargs):
    if path.startswith('hdfs:'):
        return hdfs.mkdir(path, *args, **kwargs)
    else:
        return os.mkdir(path)

os.mkdir = _poly_mkdir


def _poly_makedirs(path, *args, **kwargs):
    if path.startswith('hdfs:'):
        raise Exception('poly_open.makedirs("hdfs://...") not implemented')
    else:
        return os.mkdir(path)

os.makedirs = _poly_makedirs


def _poly_rmtree(path, *args, **kwargs):
    if path.startswith('hdfs:'):
        raise Exception('poly_open.rmtree("hdfs://...") not implemented')
    else:
        return os.mkdir(path)

shutils.rmtree = _poly_rmtree

