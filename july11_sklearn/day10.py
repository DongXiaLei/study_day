# _*_ coding: utf-8 _*_
__author__ = 'Xialei'
__date__ = '2018/7/12 8:52'
import numpy as np
from sklearn import neighbors
knn  = neighbors.KNeighborsClassifier()
data = np.array([[2,90],[3,80],[4,100],[30,1],[20,2],[30,3]]).reshape(1,-1)
label = np.array([1,1,1,2,2,2])
knn.fit(data,label)

knn.predict([1,70])
# import numpy as np
# from sklearn import neighbors
# knn = neighbors.KNeighborsClassifier()#取得knn分类器
# data = np.array([[3,104],[2,100],[1,81],[101,10],[99,5],[98,2]])
# labels = np.array([1,1,1,2,2,2])
# knn.fit(data,labels)#导入数据进行训练，data对应着打斗次数和接吻次数，而labels则是对应Romance和Action，因为这里只能接受整数类型的数组
# knn.predict([18 , 90])