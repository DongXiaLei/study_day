import numpy as np
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

iris = datasets.load_iris()
iris_X= iris.data
iris_Y= iris.target

print(iris_X[:4,:])#前面是个数，后边是属性数
print(iris_Y)#种类数

# x_train,x_test,y_train,y_test= train_test_split(iris_X,iris_Y,test_size=0.3)
# # print(y_train)
#
# knn=KNeighborsClassifier()
# knn.fit(x_train,y_train)
#
# print(knn.predict(x_test))
# print(y_test)
# print(knn.score(x_test,y_test))

from sklearn.cross_validation import cross_val_score
k_range = range(1,31)
k_score = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    #  scores = cross_val_score(knn, iris_X, iris_Y, cv=10, scoring='accuracy')
    loss = -cross_val_score(knn,iris_X,iris_Y,cv=10,scoring='mean_squared_error')
    k_score.append(loss.mean())

plt.plot(k_range,k_score)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()