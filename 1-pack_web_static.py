#!/usr/bin/python3
"""
Contain a function that generates tar file of /web_static/ dir
"""
from fabric.api import local


def do_pack():
    """Function that generates a tar of /web_static"""
    local('tar -cvzf "versions/web_static_$(date \'+%Y%m%d%H%M%S\')".tar\
            ./web_static')
