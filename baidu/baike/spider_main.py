# _*_coding:utf-8_*_
import baidu.url_manager
from baidu.baike import html_downloader, html_outputer, html_parser


class SpiderMain(object):
    def __init__(self):
        self.urls = baidu.url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlPsrser()
        self.outputer = html_outputer.HtmlOutputer()


    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count % 100 == 0:
                    self.outputer.output_html()
                    # if count == 100:
                    #     break
                count = count + 1
            except:
                print 'craw fail'
                # self.outputer.output_html()


if __name__ == "__main__":
    # 爬虫入口页面
    root_url = u"https://baike.baidu.com/item/%E5%88%9B%E6%8A%95"
    # root_url=u"https://baike.baidu.com/item/%E6%8A%95%E8%B5%84"
    # root_url=u"https://baike.baidu.com/item/%E7%BB%8F%E6%B5%8E"
    # lroot_ur = u"https://baike.baidu.com/item/%E8%AF%81%E5%88%B8"
    # root_url = u"https://baike.baidu.com/item/%e9%87%91%e8%9e%8d"
    # root_url = u"https://baike.baidu.com/item/%e5%9f%ba%e9%87%91"
    obj_spider = SpiderMain()
    # 启动爬虫
    obj_spider.craw(root_url)
