# _*_ coding: utf-8 _*_
__author__ = 'Xialei'
__date__ = '2018\7\15 0015 15:12'

import numpy as np
import pandas as pd

dates = pd.date_range('20180101',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])

df.loc['20180102','B']==2222
df.iloc[2,2]=1111
df.B[df.A>4]=0
df['F'] =np.nan
df['E'] = pd.Series([1,2,3,4,5,6],index=pd.date_range('20180101',periods=6))
print(df.fillna(value=0.1))
print(df)

data = pd.read_csv('student.csv')
print(data)

# save to
data.to_('student.pickle')