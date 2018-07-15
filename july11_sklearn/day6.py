from sklearn import preprocessing
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.datasets import make_classificaton
from sklearn.svm import SVC
import matplotlib.pyplot as plt


X,Y= make_classificaton(n_sample=300,n_feasures=2,n_redundant=0)
X =preprocessing.scale(X)
X_train,X_test,Y_train,Y_test= train_test_split(X,Y,test_size=.3)
clf =SVC()
clf.fit(X_train,Y_train)
print(clf.score(X_test,Y_test))