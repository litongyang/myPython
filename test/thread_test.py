# __author__ = 'lty'
# -*- coding: utf-8 -*-

import datetime
import os
import threading


def test(a1):
    for i in a1:
        print i


if __name__ == '__main__':
    # 需要执行的命令列表
    a = ['aaa', 'bbb', 'ccc']

    # 线程池
    threads = []

    print "程序开始运行%s" % datetime.datetime.now()
    a1 = a[0:1]
    a2 = a[1:3]
    a_n = []
    a_n.append(a1)
    a_n.append(a2)
    for n in a_n:
        th = threading.Thread(target=test, args=(n,))
        th.start()
        threads.append(th)
    # 等待线程运行完毕
    for th in threads:
        th.join()
    print len(threads)
    print "程序结束运行%s" % datetime.datetime.now()