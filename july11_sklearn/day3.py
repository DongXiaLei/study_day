import numpy as np
from numpy.random import rand
from numpy.linalg import solve, inv


x= np.array([1,2,3])
print(x)
y= np.arange(10)
print(y)
b= np.linspace(0,2,4)
print(b)
# a= np.array([1,2,3,6])
# print(a**2)
a = np.array([[1, 2, 3], [3, 4, 6.7], [5, 9.0, 5]])
a.transpose()#转化为矩阵
print(a)

# print(inv(a))
# print(solve(a,x))#解方程式at=x
c= np.dot(a,x)#a*x
print(c)