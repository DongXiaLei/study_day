# _*_ coding: utf-8 _*_
__author__ = 'Xialei'
__date__ = '2018/7/12 18:41'

import numpy as np
import matplotlib.pyplot as plt
N =10000
normal = np.random.normal(size=N)
n, bins, patches = plt.hist(normal,int(np.sqrt(N)),normed=True,lw=1)
sigma =1
mu =0
# print(bins)
plt.plot(bins,1/(sigma*np.sqrt(2*np.pi))*np.exp(-(bins-mu)**2/(2*sigma**2)),lw=4)
plt.show()
