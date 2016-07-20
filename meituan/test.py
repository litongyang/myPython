'''
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
X = np.arange(6).reshape(3, 2)
poly = PolynomialFeatures(degree=2)
print poly.fit_transform(X)
'''

'''
import matplotlib.pyplot as plt

plt.bar(left = 0,height = 1)
plt.show()
'''


import urllib
from cityid_longitude_latitude_test import cityid_pos

class P:
    def __init__(self):
        self.x = [1, 2]
        self.rank_sort = ['smart', 'solds']
        self.firstPoi = 0
        self.lastPoi = 9
        self.datekey = 20141109
        self.poiid_topk = []

    def Q(self, w, i):
        try:
            url ="http://api.mobile.meituan.com/group/v1/poi/select/hotel?cityId=%d&sort=%s&mypos=%s&cateId=20&offset=%d&limit=%d&startendday=%s~%s&client=android&utm_source=undefined&utm_medium=android&utm_term=180&version_name=4.8&utm_content=869323001086103&utm_campaign=AgroupBgroupC0E0&ci=1&uuid=0CA5AA54C17A56B5521E3D8CEBFDED1943718C8DD55572BD128DC38CA93C4CDF&msid=8693230010861031408015315260"% (int(cityid_pos[w][0]), self.rank_sort[i],  cityid_pos[w][1],  self.firstPoi, self.lastPoi, self.datekey, self.datekey)
            print
            content = urllib.urlopen(url).read()
            content = content.replace('true', 'True').replace('false', 'False').replace('null', 'None')
            test = eval(content)
            myContent_ctpois = test['ct_pois']
            for one in myContent_ctpois:
                self.poiid_topk.append(one['poiid'])
            print url
            print self.poiid_topk
        except:
            pass

if __name__ == '__main__':
    p = P()
    for i in range(0, 1):
        for j in range(0, len(cityid_pos)):
            for k in range(0, len(p.rank_sort)):
                p.Q(j, k)
                p.poiid_topk = []

'''
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
    x = "%s %s%%2c%s" % (cityid[i],latitude[i], longitude[i])
    fl.write(str(x))
    fl.write("\n")
'''

