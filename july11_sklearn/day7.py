from sklearn.learning_curve import learning_curve
from sklearn.datasets import load_digits
from sklearn.svm import  SVC
import matplotlib.pyplot as plt
import numpy as np

digits = load_digits()
X = digits.data
Y = digits.target
train_sizes,train_loss,test_loss=learning_curve(
    SVC(gamma=0.0006),X,Y,cv=10,scoring='neg_mean_squared_error',
    train_sizes=[0.1,0.25,0.5,0.75,1])
train_loss_mean = -np.mean(train_loss,axis=1)
test_loss_mean = -np.mean(test_loss,axis =1)

plt.plot(train_sizes,train_loss_mean,color="r",label ="Training")
plt.plot(train_sizes,test_loss_mean,color="g",label="cross-validation")#图表内的注释

plt.xlabel("TRAINing")#x,y的左边表示
plt.ylabel("LOSS")
plt.legend(loc="best")
plt.show()