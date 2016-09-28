# coding:utf-8

class PicManager(object):
    def __init__(self):
        self.new_pic = set()
        self.old_pic = set()

    def add_new_pic(self, url):
        if url is None:
            return
        else:
            if url not in self.new_pic and url not in self.old_pic:
                self.new_pic.add()

    def has_new_pic(self):
        return len(self.new_pic) != 0

    def get_new_pic(self):
        new_url = self.new_pic.pop()
        self.old_pic.add(new_url)
        return new_url