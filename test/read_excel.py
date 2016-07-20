# __author__ = 'tongyang.li'
# -*- coding: utf-8 -*-

import xlrd
data = xlrd.open_workbook('C:\\Users\\tongyang.li\\Desktop\\test.xlsx')
for sheet in data.sheets():
    print sheet.name
