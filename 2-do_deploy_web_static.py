#!/usr/bin/python3
""" a Fabric script that generates a .tgz archive from the contents of the
web_static folder """
from fabric.api import *
from datetime import datetime
env.hosts = ['<IP web-01>', 'IP web-02']


def do_pack():
    """ generates a .tgz archive from the contents of the web_static folder """
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)
    result = local("sudo tar -cvzf {} web_static".format(filename))
    if result.succeeded:
        return filename
    else:
        return None

def do_deploy(archive_path):
    """ distributes an archive to your web servers, using the function do_deploy """
    if not archive_path:
        return False
    else:
        put('versions/web_static_20170315003959.tgz', '/tmp/web_static_20170315003959.tgz')
        run ('mkdir -p /data/web_static/releases/web_static_20170315003959/')
        run ('tar -xzf /tmp/web_static_20170315003959.tgz -C /data/web_static/releases/web_static_20170315003959/')
        run ('rm /tmp/web_static_20170315003959.tgz')
        run ('mv /data/web_static/releases/web_static_20170315003959/web_static/* /data/web_static/releases/web_static_20170315003959/')
        run ('rm -rf /data/web_static/releases/web_static_20170315003959/web_static')
        run ('rm -rf /data/web_static/current')
        run ('ln -s /data/web_static/releases/web_static_20170315003959/ /data/web_static/current')
        put ('versions/web_static_20170315003959.tgz', '/tmp/web_static_20170315003959.tgz')
        run ('mkdir -p /data/web_static/releases/web_static_20170315003959/')
        run ('tar -xzf /tmp/web_static_20170315003959.tgz -C /data/web_static/releases/web_static_20170315003959/')
        run ('rm /tmp/web_static_20170315003959.tgz')
        run ('mv /data/web_static/releases/web_static_20170315003959/web_static/* /data/web_static/releases/web_static_20170315003959/')
        run ('rm -rf /data/web_static/releases/web_static_20170315003959/web_static')
        run ('rm -rf /data/web_static/current')
        run ('ln -s /data/web_static/releases/web_static_20170315003959/ /data/web_static/current')
