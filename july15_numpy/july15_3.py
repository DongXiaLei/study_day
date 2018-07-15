# _*_ coding: utf-8 _*_
__author__ = 'Xialei'
__date__ = '2018/7/12 15:23'
import numpy as np
from matplotlib.pyplot import plot,show

cash = np.zeros(10000)
cash[0] =1000
outcome =np.random.binomial(9,0.5,size=len(cash))

for i in range(1,len(cash)):
    if outcome[i]<5:
        cash[i]=cash[i-1]-1
    elif outcome[i]<10:
        cash[i] =cash[i-1]+1
    else:
        raise AssertionError("unexpected outcome")
print(outcome.min(),outcome.max())

plot(np.arange(len(cash)),cash)
show()
