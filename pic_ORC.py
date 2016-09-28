# coding:utf-8
# 色情图片的识别

import os
import sys, Image
import urllib


# urlretrieve(url, filename = None , reporthook = None , data = None )

class PicORC(object):
    def __init__(self):
        pass

    def pic_orc(self):
        try:
            print 'start judge'
            for i in range(0, 9999999):
                img = Image.open('{}.jpg'.format(i))
                img = img.convert('YCbCr')
                w, h = img.size
                data = img.getdata()
                cnt = 0
                for i, ycbcr in enumerate(data):
                    y, cb, cr = ycbcr
                    if 86 <= cb <= 117 and 140 <= cr <= 168:
                        cnt += 1
                print '{},jpg {} a pron image.'.format(i, 'is' if cnt > w * h * 0.3 else 'is not')
        except:
            print 'judge completed'
        return