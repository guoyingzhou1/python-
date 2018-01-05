from bs4 import BeautifulSoup

from selenium import webdriver


class padetail(object):

    def page_de(self,pageurl):
        driver = webdriver.PhantomJS(executable_path="C://Python27//phantomjs-2.1.1-windows//bin//phantomjs")
        driver.get(pageurl)

        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')

        summary_node = soup.title.get_text()
        page_nodes = soup.find_all('div', class_="ie-fix")
        con = ""
        for page in page_nodes:
            con = con + page.get_text()
        return summary_node, con
