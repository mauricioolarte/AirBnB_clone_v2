#!/usr/bin/python3
""" compress a file whit fabric """

from fabric.api import local
import datetime


def do_pack():
    """ compres a file """
    now = datetime.datetime.now()
    year = str(now.year)
    month = str(now.month)
    day = str(now.day)
    hour = str(now.hour)
    minute = str(now.minute)
    second = str(now.second)
    name_file = "web_static_" + year + month + day + hour + minute + second
    command = "sudo tar -cvzf ./versions/" + name_file + ".tgz ./web_static"
    print(name_file)
    print(command)
    local("sudo mkdir -p ./versions")
    local(command)

do_pack()
