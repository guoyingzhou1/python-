# -*- coding: utf-8 -*-
import os
import requests
import re
from lxml import etree


def StringListSave(save_path, filename, slist):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    path = save_path + "/" + filename + ".txt"
    with open(path, "w+") as fp:
        for s in slist:
            fp.write("%s\t\t%s\n" % (s[0].encode("utf8"), s[1].encode("utf8")))


def Page_Info(mypage):
    '''Regex(slowly) or Xpath(fast)'''
    dom1 = etree.HTML(mypage)
    print dom1
    urls = dom1.xpath('//div/span/a/@href')
    items = dom1.xpath('//div/span/a/text()')
    urls = urls[2:]
    del items[0]
    assert (len(items) == len(urls))
    # 组合成一个元祖
    return zip(items, urls)

def New_Page_Info(new_page):
    '''Regex(slowly) or Xpath(fast)'''
    dom = etree.HTML(new_page)

    new_items = dom.xpath('//u1/li/a/text()')
    new_urls = dom.xpath('//u1/li/a/@href')
    # 判断数量相等
    assert (len(new_items) == len(new_urls))
    # 组合成一个元祖
    return zip(new_items, new_urls)


def Doc_Info(doc_page):
    '''Regex(slowly) or Xpath(fast)'''
    ks = etree.HTML(doc_page)
    contents = ks.xpath('//p/text()')
    return contents


def Spider(url):
    i = 0
    print "downloading ", url
    # 获得url对应的源码
    myPage = requests.get(url).content.decode("gbk")
    # 通过正则获取分类标题和其对应的url
    myPageResults = Page_Info(myPage)

    save_path = u"F:/pachong/网易财经新闻抓取"
    filename = str(i) + "_" + u"财经首页"

    StringListSave(save_path, filename, myPageResults)
    i += 1
    # 获取第二层内容和url
    for item, url in myPageResults:
        print "downloading ", url
        try:
            new_page = requests.get(url).content.decode("gbk")
            # new_page = urllib2.urlopen(url).read().decode("gbk")
            if item != u"净值":
                newPageResults = New_Page_Info(new_page)

                filename = str(i) + "_" + item
                StringListSave(save_path, filename, newPageResults)
                i += 1
                for tit, dourl in newPageResults:
                    print "download", dourl
                    doc = requests.get(url).content.decode("gbk")
                    cont = Doc_Info(doc)
                    filename1 = filename + "_contents"
                    StringListSave(save_path, filename1, cont)
        except Exception:
            continue
        finally:
            print url + '下载失败'


if __name__ == '__main__':
    print "start"
    start_url = "http://money.163.com/"
    Spider(start_url)
    print "end"
