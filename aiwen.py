# -*- coding:utf-8 -*-
import time


# 获取当前时间
def getCurrentTime(self):
    return time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))


# 获取当前时间
def getCurrentDate(self):
    return time.strftime('%Y-%m-%d', time.localtime(time.time()))


if __name__ == '__main__':
    print getCurrentDate(0)
    print getCurrentTime(0)
