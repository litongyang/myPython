#__author__ = 'litongyang'
# -*- coding: utf-8 -*-

import MySQLdb
import chardet

class DOWNSTOCKDATA_DB():

    def __init__(self):
        self.file = "/Users/litongyang/Desktop/test.txt"
        self.file1 = "/Users/litongyang/Desktop/沪深Ａ股1.txt"
        self.company_code = []
        self.price = []
        self.company_code1 = []

    def createTable(self):
        for line in open(self.file):
            linone = line.split()
            self.company_code.append(linone[0])
            self.price.append(linone[2])

            my_char= chardet.detect(linone[2])
            bian_ma = my_char['encoding']
            print bian_ma
        print self.company_code
        print self.price

if __name__ == '__main__':
    downStockData_db = DOWNSTOCKDATA_DB()
    downStockData_db.createTable()