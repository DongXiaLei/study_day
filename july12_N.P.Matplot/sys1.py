import os
import sys

dic = dict()
with open(r'D:\readme.txt','r') as f:
    a= f.readline()
    while a:
        s=(a.strip()).split("-")
        s=(",".join(s)).split(",")
        for i in range(1,len(s)):
            dic[s[i]]=s[0]
        a =f.readline()
p=1
while p:
    p = input("please:")
    p= (p.strip()).lower()
    if not p: break
    if dic.get(p):
        print('the word of',p,'is' ,dic[p])
    else :
        print("no owrd")