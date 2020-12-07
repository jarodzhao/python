import numpy as np
import pandas as pd
import os

#print(np)
#print(pd)

fp=r"/storage/emulated/0/1/python/data2.csv"
for root, dirs, files in os.walk(fp):
    print(files)

# 读取csv
data=pd.read_csv(fp)
print(data.head())