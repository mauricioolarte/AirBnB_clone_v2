#!/usr/bin/python3
""" compress a file whit fabric """

from fabric.api import *
import os
import datetime

env.host = [35.185.14.17, 34.73.91.94]


def do_pack():
    """ compres a file """
    try:
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
        file = local(command)
        return file
    except:
        return(None)


def def do_deploy(archive_path):
    """ deploy files in server """
    if os.path.isfile(archive_path):
        try:
            put(archive_path, "/temp/")
            destini_path = "/data/web_static/releases/" + archive_path.strip(".tgz") + "/"
            run("mkdir -p {}".format(destini_path))
            run("tar -xvzf /tmp/{} -C {}".format(archive_path.split("/")[-1], destini_path))
            run("rm /tmp/{}".format(archive_path.split("/")[-1]))
            run("mv {}/web_static/* {}".format(destini_path, destini_path))
            run("rm {}/web_static".format(destini_path))
            run("rm -rf /data/web_static/current")
            run("ln -s {} /data/web_static/current")
            return(True)
        except:
            return(False)
    else:
        return(False)
