# -*- coding: utf-8 -*-
import pandas as pd
data = pd.read_csv(r"c:\data.csv")
print data
data.set_index('地区',inplace=True)
data.head(10)
