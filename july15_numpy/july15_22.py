# _*_ coding: utf-8 _*_
__author__ = 'Xialei'
__date__ = '2018\7\15 0015 15:00'

import numpy as np
import pandas as pd

dates = pd.date_range('20180101',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])

print(df['A'],df.A)
print(df[0:3])

print(df.loc['20180101'])
print(df.loc['20180101',['A','B']])

print(df.iloc[[1,3,5],1:3])
print(df.iloc[3:5,1:3])

print(df[df.A>8])
