# _*_ coding: utf-8 _*_
__author__ = 'Xialei'
__date__ = '2018\7\15 0015 13:24'

import numpy as np
A = np.arange(3,15).reshape((4,3))

print(A)
print(A[3][1],A[3,1],A[3,:2])
print(A.flatten())
# array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

for item in A.flat:
    print(item)

a = np.array([1,1,1])
aa = a[:,np.newaxis]
print(aa)
b = np.array([2,2,2])
c = np.vstack(((a,b)))
d = np.hstack(((a,b)))
print(c,c.shape)
print(d,d.shape)
e =np.concatenate((a,b,b,a),axis=0)
print(e)

A = np.arange(12).reshape((3,4))
print(np.split(A,2,axis=1))#在列上分均等的两份
print(np.array_split(A,3,axis=1))
print(np.vsplit(A,3))#水平均等分割
print(np.hsplit(A,2))

a = np.array([1,1,3])
b = a
a[1] =11
print(a,b)
b =a.copy()
a[1]=2
print(a,b)