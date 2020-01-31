# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 14:54:52 2019

@author: BerkeAyevi
"""

file= open('matrix.txt')
f = file.read()
w= f.split('\n')#split with respect to enter
x=[]
y=[]
for i in w:
    u=i.split('\t')#split with respect to tap
    x.append(u)
for i in x:
    p=list(map(float,i))#str to float
    y.append(p)

print(y)
