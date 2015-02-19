#-*- coding:utf-8 -*-
import os, time


def avatarFile(instance, filename):
    name, ext = os.path.splitext(filename)
    return "avatars/%s-%s%s" % (instance.username, name[:3], ext)