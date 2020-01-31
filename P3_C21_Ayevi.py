# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:48:35 2019

@author: BerkeAyevi
"""

file = open("data.txt",'r')
f = file.read()
w=f.split()
a=[]
b=[]
x=[]
y=[]
m=[]
q =[]
def space(x):#spacing row
    u = ' ' * (int(x))+ '**'
    return u 

def dash(x): #dash row
    oo = '_'+'___' * int(x)
    return oo

def qqq(x,y):
    i=0
    while (len(x)>i):
        if (x[i]==y):
            return (i+1)#i+1 olması gerekir ama
            break
        
        else:
            i=i+1
            continue
def sol(x): #scaling last row
    if (x<10):
        return print(" {}|".format(int(x)))
    else:
        return print("{}|".format(int(x)))

for i in w: #reading file
    a.append(float(i))


for e in range(len(a)): #spliting x and y  
    if (e%2==0):
        x.append(a[e])
    else:
        y.append(a[e])

for i in range(0,int(max(y))):
    u = int(max(y))-i
    m.append([u])
for i in range(0,len(m)):
    c=int(max(y))-int(i)
    if (qqq(y,c)):
        m[i].append(space(qqq(y,c)))
    else:
        continue
for i in range(0,len(m)):
    if(int(m[i][0])<10):
        if (len(m[i])==2):
            print(" {}|{}".format(m[i][0],m[i][1]))
        else:
            print(" {}|".format(m[i][0]))
    else:
        if (len(m[i])==2):
            print("{}|{}".format(m[i][0],m[i][1]))
        else:
            print("{}|".format(m[i][0]))

print("  +{}".format(dash(len(x))))
print("  ",end='')

for z in range(1,len(x)):
    print("  {}".format(z), end=' ')
    
   
