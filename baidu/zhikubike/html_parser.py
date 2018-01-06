# _*_coding:utf-8_*_
from bs4 import BeautifulSoup
import urlparse
import re


class HtmlPsrser(object):
    # 找到页面中所有的url,相对路径的url转换成绝对路径的url
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/wiki/(.*)"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}

        res_data['url'] = page_url

        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('h1', class_='firstHeading')
        res_data['title'] = title_node.get_text()

        para_nodes = soup.find('div', id='bodyContent').find_all('p')
        str1 = ""
        for para_node in para_nodes:
            str1 = str1 + para_node.get_text()
        res_data['contents'] = str1

        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'lxml', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
