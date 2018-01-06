# _*_coding:utf-8_*_


import urllib2


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        # 下载网页，也可以用异常抛出
        response = urllib2.urlopen(url, timeout=3)

        if response.getcode() != 200:
            return None

        return response.read()
