# _*_ coding: utf-8 _*_
__author__ = 'Xialei'
__date__ = '2018\7\15 0015 16:03'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# datas = pd.Series(np.random.randn(1000),index=np.arange(1000))
# datas = datas.cumsum()
# # print(datas)
# # datas.plot()
# # plt.show()

data = pd.DataFrame(
    np.random.randn(100,4),
    index=np.arange(100),
    columns=list("ABCD")
    )
data =data.cumsum()
ax = data.plot.scatter(x='A',y='B',color='DarkBlue',label='Class1')
# 将之下这个 data 画在上一个 ax 上面
data.plot.scatter(x='A',y='C',color='LightGreen',label='Class2',ax=ax)
plt.show()
data.plot()
plt.show()