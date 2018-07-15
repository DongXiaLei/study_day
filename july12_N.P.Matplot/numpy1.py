import numpy as np

array = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
print(array)
print('dim:',array.ndim)
print('shape:',array.shape)
print("size:",array.size)

a = np.ones((3,4),dtype=float)
b = np.arange(0.5,7,2).reshape((2,2))
c = np.linspace(1,5,12).reshape((3,4))
print(a)
print(b)
print(c)

e = np.array([1,2,3,4]).reshape((2,2))
f = np.arange(4).reshape((2,2))
ans = e+f
anss= e-f
ansss=e*f#单独相乘
print(f==3)
test = e*f
test_dot=np.dot(e,f)
print(test,test_dot)