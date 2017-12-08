# _*_coding:utf-8_*_
import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
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

                if count == 10:
                    break
                count = count + 1
            except:
                print 'craw fail'
        self.outputer.output_html()

if __name__ == "__main__":
    # 爬虫入口页面
    # root_url = 'http://baike.baidu.com/item/scala'
    root_url=u"https://baike.baidu.com/item/%e9%87%91%e8%9e%8d"
    obj_spider = SpiderMain()
    # 启动爬虫
    obj_spider.craw(root_url)