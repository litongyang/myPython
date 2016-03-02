# __author__ = 'litongyang'
# -*- coding: utf-8 -*-

name = []
ID = []
ID_name = {}

for line in open("C:\\Users\\Thinkpad\\Desktop\\wuxi-home\\base.txt"):
    linone = line.split('\t')
    ID.append(linone[0])
    name.append(linone[2].decode('gb2312', 'ignore').encode('utf-8'))

ID_top = []
for line in open("C:\\Users\\Thinkpad\\Desktop\\com_top.txt"):
    linone = line.split('\n')
    ID_top.append(linone[0])
# print ID_top

fl = open("C:\\Users\\\Thinkpad\\Desktop\\company_id_name.txt", 'w')
fl.write("id")
fl.write("\t")
fl.write("name")
fl.write("\n")
for id in ID_top:
    for i in range(0, len(ID)):
        if ID[i] == id:
            fl.write(id)
            fl.write('\t')
            fl.write(name[i])
    fl.write('\n')