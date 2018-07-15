import  matplotlib.pyplot as plt
import  numpy as np
import Django

x=np.linspace(-1,1,50)
y1=2*x+1
y2=2**x

plt.figure()
plt.plot(x,y1,color='r',linewidth=2.0,linestyle='--')

plt.figure(num=3,figsize=(8,5))
plt.plot(x,y2,label='up')
plt.plot(x,y1,color='r',linewidth=1.0,label='down')
plt.legend()

plt.show()