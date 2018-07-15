# _*_ coding: utf-8 _*_
__author__ = 'Xialei'
__date__ = '2018/7/14 21:44'
import numpy as np

# #以下均返回矩阵[1 2 3]列表[1,2,3]
# array =np.array([[1,2,3],[2,3,4]])
# print(array.ndim,array.shape,array.size,array.sort())
#
# a = np.zeros((3,4))
# b = np.ones((3,4))
# c = np.empty((3,4))
# d = np.arange(1,12,2).reshape((2,3))
# e = np.linspace(1,10,4).reshape((2,2))
#
# x= np.array([[1,2],[3,4]])
# y =np.arange(4).reshape((2,2))
# print(y<2,x==3)
# print(x)
# print(y)
# print(x*y)
# print(x**2)
# print(np.sin(x))
# print(np.dot(x,y))
# print(x.dot(y))
#
# a = np.random.random((2,4))
# print(a)
# print(np.sum(a,axis=1))
# print(np.max(a,axis=0))
# print(np.min(a,axis=1))

A= np.arange(12).reshape((3,4))

print(A)
print(np.sum(A),A.sum())
print(np.mean(A),A.mean(),np.average(A))
print(np.median(A))
print(np.argmin(A))
print(np.argmax(A))#矩阵中最小元素和最大元素的索引
print(np.cumsum(A))#每一项都是加到本位置的值，返回一维矩阵
print(np.diff(A))

A = np.arange(14,2, -1).reshape((3,4))
print(A)
print(np.sort(A))  #按行排序
print(np.transpose(A))
print(A.T)
print(np.clip(A,9,5))