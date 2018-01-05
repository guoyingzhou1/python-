# _*_coding:utf-8_*_

from pymongo import MongoClient


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
        self.ko1 = 1
        self.ig = 1

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        # 保存到mongodb
        """

        :rtype: object
        """
        for data in self.datas:
            client = MongoClient('192.168.1.225')
            db = client.log
            db.authenticate('hadoopUser', '123')  # 验证用户名密码
            posts = db.wenku
            posts.save(data)
        self.datas = []
        print '第' + str(self.ig) + '次存储'
        self.ig += 1
