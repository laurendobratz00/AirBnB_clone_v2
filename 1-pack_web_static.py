#!/usr/bin/python3
""" a Fabric script that generates a .tgz archive from the contents of the
web_static folder """
from fabric.api import *
from datetime import datetime


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
