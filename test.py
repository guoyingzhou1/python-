# -*- coding: utf-8 -*-
import re
import urllib2

from bs4 import BeautifulSoup

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  # 初始化headers
headers = {'User-Agent': user_agent}
i = 0
urlarr = []
while len(urlarr) < 6:
    url = "https://wenku.baidu.com/jingpin/147?ca=147&od=3&pn=" + str(i)
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    # print response.getcode()
    ht = response.read()
    pattern = re.compile('span class="ic ic-doc".*?href="(.*?)"', re.S)
    items = re.findall(pattern, ht)
    for oldurl in items:
        newurl = "https://wenku.baidu.com" + oldurl
        urlarr.append(newurl)
    print i
    i += 6
