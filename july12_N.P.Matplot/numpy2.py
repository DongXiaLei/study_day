import numpy as np

a = np.random.random((3,3))#不说明在（0,1）之间
print(a[2][2],a[2,2])
print(a[:,2])
print(a.flatten())
for item in a.flat:#迭代器
    print(item)

print(a)
# print(np.sum(a,axis=1))#axis=1在每一行处理 0位每一列处理
# print(np.min(a,axis=0))
# print(np.max(a,axis=1))
#
# b = np.arange(1,13).reshape((3,4))
# print(np.argmin(b),np.argmax(b))#索引
# print(np.average(b))
# print(np.mean(b,axis=0))
# print(b)
# # print(np.diff(b))#行之间线差值
# # print(np.sort(b))#行之间排序
# # print(np.cumsum(b))#输出每加一项的值
# # print(np.nonzero(b))
# print(b.T,np.transpose(b))
# print(np.transpose(b).dot(b))
# print(np.clip(b,5,9))