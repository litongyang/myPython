# __author__ = 'lty'
# -*- coding: utf-8 -*-

import pyhdfs
f = pyhdfs.HdfsClient(hosts='hdp1.fengjr.inc:8020')
print f.list_status('/')