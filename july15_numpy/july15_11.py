# _*_ coding: utf-8 _*_
__author__ = 'Xialei'
__date__ = '2018\7\15 0015 13:57'

import pandas as pd
import numpy as np
s = pd.Series([1,3,34,np.nan,46])#一维
print(s)
dates = pd.date_range('20180101',periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
print(df,df['b'])
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})

print(df2,df2.dtypes,df2.index,df2.columns)
print(df2.values,df2.describe())
print(df2.sort_index(axis=1, ascending=False))
print(df2.sort_values(by='E'))
