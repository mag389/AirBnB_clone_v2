#!/usr/bin/python3
""" packing all files """
from fabric.api import *
from datetime import datetime
import os


env.hosts = ['35.227.79.31', '35.243.199.170']


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
            run("sudo mkdir -p /data/web_static/releases/{}/".format(noext[0]))
            run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
                format(fname[1], noext[0]))
            run("sudo rm /tmp/{}".format(fname[1]))
            run("sudo mv /data/web_static/releases/{}/web_static/*\
                 /data/web_static/releases/{}/".format(noext[0], noext[0]))
            run("sudo rm -rf /data/web_static/releases/{}/web_static".
                format(noext[0]))
            run("sudo rm -rf /data/web_static/current")
            run("sudo ln -s /data/web_static/releases/{}/\
                 /data/web_static/current".format(noext[0]))
            return True
        except Exception as e:
            # print(e)
            return False
    return False


def deploy():
    """ deploy the archive entirely"""
    arcname = do_pack()
    if arcname is None:
        return False
    return do_deploy(arcname)


def do_clean(number=0):
    """ cleans up the repos of old versions YmdMHS """
    numb = int(number)
    if numb <= 1:
        numb = 1
    numb += 1
    listy = local('sudo ls -1t ./versions/web_static_*.tgz | \
        sudo tail -n+{} | \
        sudo tr "\n" " " | \
        sudo xargs rm -rf'.format(numb))
    run('sudo ls -1t /versions/web_static/releases/web_static_*.tgz | \
        sudo tail -n+{} | \
        sudo tr "\n" " " | \
        sudo xargs rm -rf'.format(numb))
