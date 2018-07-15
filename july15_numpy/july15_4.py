# _*_ coding: utf-8 _*_
# __author__ = 'Xialei'
# __date__ = '2018/7/1# _*_ coding: utf-8 _*_
import numpy as np
import matplotlib.pyplot as plt
import os
import math
a = math.pi/2
x = np.linspace(0, a, 1000)
y = np.sqrt(np.sin(2*x) * np.sin(x))

file = open(r'C:\Users\15940\Desktop\readme.txt','r')
striing = file.readlines()
print(striing)


# plt.plot(x,y)
# plt.show()2 18:40'