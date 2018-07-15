from sklearn.learning_curve import validation_curve
from sklearn.datasets import load_digits
from sklearn.svm import  SVC
import matplotlib.pyplot as plt
import numpy as np

digits = load_digits()
X = digits.data
Y = digits.target

param_rang = np.logspace(-6,-2.3,5)
train_loss,test_loss=validation_curve(
    SVC(),X,Y,param_name='gamma',param_range=param_rang,cv=10,scoring='neg_mean_squared_error')
train_loss_mean = -np.mean(train_loss,axis=1)
test_loss_mean = -np.mean(test_loss,axis =1)

plt.plot(param_rang,train_loss_mean,color="r",label ="Training")
plt.plot(param_rang,test_loss_mean,color="g",label="cross-validation")#图表内的注释

plt.xlabel("Gamma")#x,y的左边表示
plt.ylabel("LOSS")
plt.legend(loc="best")
plt.show()