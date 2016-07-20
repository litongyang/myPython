# __author__ = 'tongyang.li'

import urllib
import os
url = 'http://pdf.dfcfw.com/pdf/H3_AP201607050016383683_1.pdf'
path = 'test.pdf'
f = open(path, 'wb')
urllib.urlretrieve(url, path)