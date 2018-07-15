# _*_ coding: utf-8 _*_
__author__ = 'Xialei'
__date__ = '2018/7/12 20:03'

# import pandas
# import io
# file =open(r'C:\Users\15940\Desktop\liris.txt','r')
# df =file.read()
# print(df)
# print(len(df))
from pandas import read_csv

df = read_csv(r'C:\Users\15940\Desktop\dataset\SampleCSV_files\AssetsImportCompleteSample.csv')
print(df.shape)
print(len(df))
print(df.columns,df.dtypes)