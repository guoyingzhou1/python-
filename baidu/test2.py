import re
import urllib2
import urlparse


def _get_new_urls(page_url, soup):
    new_urls = set()
    # links = soup.find_all('a', href=re.compile(r"/item/\d+\.html"))
    links = soup.find_all('a', href=re.compile(r"/view/(.*)"))
    for link in links:
        new_url = link['href']
        new_full_url = urlparse.urljoin(page_url, new_url)
        new_urls.add(new_full_url)
    return new_urls

if __name__ == "__main__":
    i=0
    url = "https://wenku.baidu.com/jingpin/147?ca=147&od=3&pn="+str(i)
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    # print response.getcode()
    ht = response.read()
    nurls = _get_new_urls(url, ht)