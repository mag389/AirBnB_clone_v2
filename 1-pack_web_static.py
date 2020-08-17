#!/usr/bin/python3
""" packing all files """
from fabic.api impoort *
from datetime import datetime
import os


def do_pack():
    """ packs all files to a tgz file from web_static folder"""
    now = datetime.now()
    dt = now.strftime("%Y%m%d%H%M%S")
    fname = "web_static_" + dt + ".tgz"
    local("mkdir -p versions")
    local("tar -cvf {} web_static".format(fname))
    if os.path.exists(fname):
        return fname
    return None
