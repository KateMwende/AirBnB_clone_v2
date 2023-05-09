#!/usr/bin/python3
"""
distributes an archive to your web servers
"""
import os
from fabric.api import *

env.hosts = ["
