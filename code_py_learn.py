#!/usr/bin/env python
# _*_ coding:UTF-8 _*_
import random,os,sys
from you_get.extractors import netease

class playnetease(object):
    def __init__(self):
        pass
    def music(self):
        netease.netease_cloud_music_download("https://music.163.com/#/song?id=501133611",info_only=True)
if __name__ == '__main__':
    s = playnetease()
    s.music()