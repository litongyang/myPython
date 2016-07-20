#__author__ = 'litongyang'
# -*- coding: utf-8 -*-
cityName = []
cityID1 = []
cityName1 = []
Longitude1 = []
Latitude1 = []
name = []
id = []
Longitude = []
Latitude = []

for line in open("/Users/litongyang/Desktop/city.txt"):
    linone = line.split()
    cityName.append(linone[0])
    Longitude1.append(linone[1])
    Latitude1.append(linone[2])


for line in open("/Users/litongyang/Desktop/cityID1.txt"):
    linone = line.split()
    cityID1.append(linone[0])
    cityName1.append(linone[1])

len1 = cityName1.__len__()
len = cityName.__len__()

for i in range(0, len1):
    for k in range(0, len):
        if cityName1[i] in cityName[k]:
            name.append(cityName1[i])
            id.append(cityID1[i])
            Longitude.append(Longitude1[k])
            Latitude.append(Latitude1[k])
len_name = name.__len__()
fl = open("/Users/litongyang/Desktop/city_Longitude_Latitude.txt", 'wr')
fl.write("cityid    cityname  Longitude  Latitude")
fl.write('\n')
for i in range(0, len_name, 1):
    fl.write(str(id[i]))
    fl.write("\t")
    fl.write(str(name[i]))
    fl.write("\t")
    fl.write(str(Longitude[i]))
    fl.write("\t")
    fl.write(str(Latitude[i]))
    fl.write("\n")

fl.close()