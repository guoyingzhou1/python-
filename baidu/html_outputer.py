# _*_coding:utf-8_*_
import os
from pymongo import MongoClient


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        # 保存成网页形式
        fout = open('output.html', 'w')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td style='width:400px'>%s</td>" % data['url'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        # 保存为文件
        filename = u'kaf'
        save_path = u'F:/pachong/'
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        path = save_path + "/" + filename + ".txt"
        with open(path, "w+") as fp:
            for s in self.datas:
                fp.write("%s\n" % (s['summary'].encode('utf8')))
        # 保存到mongodb
        for data in self.datas:
            client = MongoClient('192.168.1.225')
            db = client.log
            db.authenticate('hadoopUser', '123')  # 验证用户名密码
            posts = db.haha
            posts.save(data)
