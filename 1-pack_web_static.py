#!/usr/bin/env python3
"""
Contain a function that generates tar file of /web_static/ dir
"""
from fabric.api import local


def do_pack():
    """Function that generates a tar of /web_static"""
    try:
        local(
                'tar -cvzf "versions/web_static$(date \'+%Y%m%d%H%M%S\')".tar\
                ./web_static')
        return "versions/"
    except Exception:
        return None
