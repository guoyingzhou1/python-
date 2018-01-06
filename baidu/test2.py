import re
import urllib2
import urlparse

from bs4 import BeautifulSoup

# def _get_new_urls(page_url, soup):
#     new_urls = set()
#
#     links = soup.find_all('a', href=re.compile(r"/wiki/(.*)"))
#     for link in links:
#         new_url = link['href']
#         new_full_url = urlparse.urljoin(page_url, new_url)
#         new_urls.add(new_full_url)
#     return new_urls

if __name__ == "__main__":
    # url = "http://money.163.com/18/0106/08/D7F0RFS3002581PP.html"
    # user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    # headers = {'User-Agent': user_agent}
    # request = urllib2.Request(url, headers=headers)
    # response = urllib2.urlopen(request)
    # # print response.getcode()
    # ht = response.read()
    # soup = BeautifulSoup(ht, 'lxml')
    #
    # # nurls=_get_new_urls(url,soup)
    # contents=soup.find('div',class_='post_text').find_all('p')
    # str=""
    # for k in contents:
    #     str=str+k.get_text()

    new_url="http://money.163.com/special/view749/"
    if re.match(r"http://money.163.com/1[0-9]/(.*)", new_url):
        print 'good'
