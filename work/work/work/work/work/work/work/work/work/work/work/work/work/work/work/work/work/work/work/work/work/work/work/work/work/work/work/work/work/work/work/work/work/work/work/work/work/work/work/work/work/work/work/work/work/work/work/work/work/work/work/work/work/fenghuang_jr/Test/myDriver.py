# __author__ = 'tongyang.li'
# !/usr/local/lib/python2.7

import os
import MySQLdb


class Driver:
    def __init__(self):
        self.url = "jdbc:hive2://10.10.202.13:10000/default"
        self.user_name = ""
        self.pass_word = ""

    # noinspection PyBroadException
    def link_hive(self):
        print "test!"
        try:
            conn = MySQLdb.connect(host=self.url, user=self.user_name, passwd=self.pass_word)
            cur = conn.cursor()
            cur.execute('set names \'utf8\'')
        except Exception, e:
            print Exception, e

if __name__ == '__main__':
    test = Driver()
    test.link_hive()
