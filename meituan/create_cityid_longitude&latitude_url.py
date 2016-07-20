#__author__ = 'litongyang'

cityid = []
longitude = []
latitude = []
result = []
for line in open("/Users/litongyang/Desktop/cityid_Longitude_Latitude.txt"):
     linone = line.split()
     cityid.append(linone[0])
     longitude.append(linone[1])
     latitude.append(linone[2])
print type(longitude[0])
fl = open("/Users/litongyang/Desktop/test02.txt", 'wr')
cityid_len = cityid.__len__()
for i in range(0, cityid_len):
    x = "[%s, '%s%%2c%s']," % (cityid[i],latitude[i], longitude[i])
    fl.write(str(x))
    fl.write("\n")
