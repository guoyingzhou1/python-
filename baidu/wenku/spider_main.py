# -*- coding: utf-8 -*-

import re
import urllib2

import baidu.wenku.wenku_outputer
from baidu.wenku import page_detail


class spider_main(object):
    def __init__(self):
        self.contents = page_detail.padetail()
        self.outputer = baidu.wenku.wenku_outputer.HtmlOutputer()

    def craw_con(self, ursour):
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  # 初始化headers
        headers = {'User-Agent': user_agent}
        i = 0
        while i < 1195:
            try:
                url = ursour + str(i)
                request = urllib2.Request(url, headers=headers)
                response = urllib2.urlopen(request)
                # print response.getcode()
                ht = response.read()
                pattern = re.compile('span class="ic ic-doc".*?href="(.*?)"', re.S)
                items = re.findall(pattern, ht)
                print 'craw第'+str(i)+'页数据'

                for oldurl in items:
                    newurl = 'https://wenku.baidu.com' + oldurl
                    title, data = self.contents.page_de(newurl)
                    res_data = {}
                    res_data['url'] = newurl
                    res_data['title'] = title
                    res_data['content'] = data
                    self.outputer.collect_data(res_data)
                i += 6
                if i % 30 == 0:
                    self.outputer.output_html()
            except:
                print "craw fail"
if __name__ == "__main__":
    ursour = "https://wenku.baidu.com/jingpin/146?ca=146&od=3&pn="
    ko = spider_main()
    ko.craw_con(ursour)
