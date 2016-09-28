# coding:utf-8

import os
import urllib

def schedule(a, b, c):
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print '%.2f%%' % per

class PicDownload(object):
    def __init__(self):
        self.count = 0

    def download_all_pic(self, pic_urls):
        for link in pic_urls:
            urllib.urlretrieve(link, '{}.jpg'.format(self.count), schedule)
            self.count += 1



