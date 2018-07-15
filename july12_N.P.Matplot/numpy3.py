import  numpy as np

A = np.array([1,1,1])[:,np.newaxis]
C = A[:,np.newaxis]
B = np.array([2,2,2])[:,np.newaxis]
print(np.vstack((A,B)))#vertical stack
print(np.hstack((A,B)))#horizonal stack
print(np.concatenate((A,B,A,B),axis=1))

a = np.arange(12).reshape((3,4))
print(a)
print(np.split(a,3,axis=0))
print(np.vsplit(a,3))
print(np.hsplit(a,4))
