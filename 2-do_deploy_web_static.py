#!/usr/bin/python3
""" a Fabric script that generates a .tgz archive from the contents of the
web_static folder """
from fabric.api import *
from datetime import datetime
env.hosts = ['34.73.89.226', '18.212.230.41']


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
    split_path = archive_path.split("/")[-1]
    filename = '/data/web_static/releases/' + "{}".format(split_path.split('.')[0])
    tmp = "/tmp/" + split_path

    try:
        put(archive_path, "/tmp/")
        run ('mkdir -p {}/'.format(filename))
        run ('tar -xzf {} -C {}/'.format(tmp, filename))
        run ('rm {}'.format(tmp))
        run ('mv {}/web_static/* {}/'.format(filename, filename))
        run ('rm -rf {}/web_static'.format(filename))
        run ('rm -rf /data/web_static/current')
        run ('ln -s {}/ /data/web_static/current'.format(filename))
        return True
    except:
        return False
