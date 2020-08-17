#!/usr/bin/python3
""" packing all files """
from fabric.api import *
from datetime import datetime
import os


env.hosts = ['35.227.79.31']  # , '35.243.199.170']


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


def do_deploy(archive_path):
    """ distrubutes an archive to web servers """
    if os.path.exists(archive_path):
        try:
            # print("into try")
            put(archive_path, "/tmp/")
            fname = archive_path.split("/")
            noext = fname[1].split(".")
            # print(fname)
            run("mkdir -p /data/web_static/releases/{}".format(noext[0]))
            run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".
                format(fname[1], noext[0]))
            run("rm /tmp/{}".format(fname[1]))
            run("rm -f /data/web_static/current")
            run("sudo ln -sf /data/web_static/releases/{}\
                 /data/web_static/current".format(noext[0]))
            return True
        except Exception as e:
            # print(e)
            return False
    return False
