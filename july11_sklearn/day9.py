# _*_ coding: utf-8 _*_
__author__ = 'Xialei'
__date__ = '2018/7/12 9:09'
from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import tree
from sklearn import preprocessing
from sklearn.externals.six import StringIO

allElectronicsData = open(r"D:\workspace\python\files\AllElectronics.csv")

reader = csv.reader(allElectronicsData)
headers = reader.next()
print (headers)
featureList = []
labelList = []

for row in reader:
    labelList.append(row[len(row)-1])
    rowDict = {}
    for i in  range(1,len(row)-1):
        rowDict[headers[i]]=row[i]
    featureList.append(rowDict)
print (featureList)
#Vetorrize features
vec = DictVectorizer()
dummyX = vec.fit_transform(featureList).toarray()
print ("dummyx:" + str(dummyX))
print (vec.get_feature_names())

print ("labelList:" + str(labelList))
# vectorize class labels
lb =preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)
print ("dummyY:"+ str(dummyY))

#Using decision tree for classification
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf =clf.fit(dummyX,dummyY)
print ("clf:"+str(clf))

#Visualize mpdel
with open("allElectornicinformationGainOri.dot",'w')as f:
    f = tree.export_graphviz(clf,feature_names=vec.get_feature_names(),out_file=f)
#dot 转化成pdf 树：dot -Tpdf " " -o output.pdf
oneRowx = dummyX[0,:].reshape(1, -1)
print ("oneRowx"+str(oneRowx))
#测试模型
newRowX = oneRowx
#这里有个坑，一定要注意维度 numpy！！！
newRowX[0][0] = 0
newRowX[0][2] = 1
newRowX.reshape(1, -1)
print ("newRowx:" + str(newRowX))
predictedY = clf.predict(oneRowx)
print ("predictedY"+str(predictedY))