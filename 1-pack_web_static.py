#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from
the contents of the web_static folder of your AirBnB Clone repo
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    generates a .tgz archive
    """
    try:
        local("mkdir -p versions")
        timestamp = datetime.now().strftime("%Y%m%d%H%M%s")
        archive_path = ("versions/web_static_{}.tgz".format(timestamp)) 
        local("tar -cvzf versions/web_static_{}.tgz web_static/".format(timestamp))
        return (archive_path)
    except Exception as e:
        return None
