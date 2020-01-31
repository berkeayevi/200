# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 17:32:25 2019

@author: BerkeAyevi
"""
while True:
    def find_roots(a,b,c):
        
        delta = (b**2) - (4* a* c)
        
        if (delta>0):
            sd = (delta)**(1/2)
            x1=((-1*b)-(sd))/(2*a)
            x2=((-1*b)+(sd))/(2*a)
            return print("{}, {}".format(x1,x2))
        elif(delta<0):
            sd = (-delta)**(1/2)
            x1=(-1*b)/(2*a)
            x1im=(sd)/(2*a)
            x2=(-1*b)/(2*a)
            x2im=(sd)/(2*a)
            return print("({}-{}i),({}+{}i)".format(x1,x1im,x2,x2im))
        else:
            x1 =(-1*b)/(2*a)
            return print("There is a single real root: {}".format(x1))
            
    x=[]
    z=[]
    print("\nRoot finding for ax^2+bx+c you will give input a, b and c with comma \nfor exit give input 99")
    p = [input("Enter coefficients: ")]
    
    
    for i in p:
        u= i.split(',')
        z.append(u)
    ber= len(z[0])#eğer dicen 3 veye 4 2 falan ise false döndür
    for j in range(0,ber):
        p = (z[0][j])
        x.append(float(p))
    if(x[0]==99 and len(x)==1):
        break
    elif (len(x)>3):
        print("You must enter three integers")
    elif(len(x)<3):
        print("You must enter three integers")
    else:
        if(x[0]==0):
            print("Not a quadratic polynomial.")
        else:
            a=x[0]
            b=x[1]
            c=x[2]
            find_roots(a,b,c)
        
    
    
        




    
