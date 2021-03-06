#!/usr/bin/python3
""" packing all files """
from fabric.api import *
from datetime import datetime
import os


def do_pack():
    """ packs all files to a tgz file from web_static folder"""
    now = datetime.now()
    dt = now.strftime("%Y%m%d%H%M%S")
    fname = "versions/web_static_{}.tgz".format(dt)
    local("mkdir -p versions")
    local("tar -czvf {} web_static".format(fname))
    if os.path.exists(fname):
        return fname
    return None
