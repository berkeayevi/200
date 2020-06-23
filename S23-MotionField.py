# -*- coding: utf-8 -*-
"""
Created on Sun May 17 13:29:58 2020

@author: BerkeAyevi
"""

def cross(v1,v2):    
    i=v1[1]*v2[2]-v1[2]*v2[1]
    j=v1[2]*v2[0]-v1[0]*v2[2]
    k = v1[0]*v2[1]-v1[1]*v2[0]    
    product=[i,j,k]    
    return product
def add (v1,v2):
    i=v1[0]+v2[0]
    j=v1[1]+v2[1]
    k=v1[2]+v2[2]
    added=[i,j,k]
    return added
def mult(x,v):
    i=x*v[0]
    j=x*v[1]
    k=x*v[2]
    multi=[i,j,k]
    return multi

q = -1.602*(10**-19)  #charge of electron
m=  9.10938 * (10**-31) #mass of electron

E= [1*10**-19,1*10**-19,1*10**-19]
B= [3*10**-19,99999*10**-19,70*10**-19]
r= [0,0,0]
v= [0,0,0]
t =[]
i=1
ms = 1/m # bir daha bölme için fonk yazmamak için
    
file= open('S23.txt','w')
while(i<100):
    
    f = mult(q,add(E,cross(v,B)))
    a = mult(ms,f) #accelartionn
    v = add(mult(i,a),v)
    r = add(mult(i,v),r)
    for j in range(0,3):
        file.write("{} ".format(r[j]))
    file.write("\n")
    i = i+1

file.close()

