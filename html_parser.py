# coding:utf-8

import re
from bs4 import BeautifulSoup
import urlparse
import urllib2


class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # read-13369-1-1.html id="normalthread_13744"
        # find_all( name , attrs , recursive , text , **kwargs )
        links = soup.find_all(attrs = {'class': 's xst', 'href': re.compile(r"read-\d+-1-1\.html")})
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin('http://www.qqqav9090.net', new_url)
            new_urls.add(new_full_url)
        return new_urls

    def url_parse(self, page_url):
        if page_url is None:
            return

        response = urllib2.urlopen(page_url)
        if response.getcode() != 200:
            return None
        html_cont = response.read()
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding = 'utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        return new_urls

    def pic_parse(self, page_url):
        pic_urls = set()
        # http://luntan.tan5959.com/forum/201604/10/200737l7jiqotkk2x7t9jk.jpg
        # id="postmessage_13744"

        response = urllib2.urlopen(page_url)
        if response.getcode() != 200:
            return None
        html_cont = response.read()
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding = 'utf-8')
        links = soup.find_all(attrs={'class': 'zoom'})
        for link in links:
            new_url = link['file']
            pic_urls.add(new_url)
        return pic_urls