# coding:utf-8

import pic_download, pic_ORC, url_manager, html_parser, pic_manager

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.download = pic_download.PicDownload()
        self.parser = html_parser.HtmlParser()
        self.ORC = pic_ORC.PicORC()
        self.pics = pic_manager.PicManager()
        # self.initparser = initparser()


    def craw(self, root_url):
        count = 1
        # self.urls.add_new_url(root_url)
        new_urls = self.parser.url_parse(root_url)

        # 暂时加上，以后拓展时候改
        for url in new_urls:
            self.urls.add_new_url(url)

        count = 1
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'add {}st url {}'.format(count, new_url)
                pic_urls = self.parser.pic_parse(new_url)
                self.download.download_all_pic(pic_urls)

                '''
                self.pics.add_new_pics(pic_urls)

                while self.pics.has_new_pic():
                    new_pic = self.pics.get_new_pic()
                    self.ORC.pic_orc(new_pic)   # new_pic is a link
                '''

                '''
                if count == 10:
                    break
                    count += 1
                '''
                count += 1
            except:
                print 'craw fail'

        self.ORC.pic_orc()

if __name__ == "__main__":
    root_url = "http://www.qqqav9090.net/forum-49-1.html"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
