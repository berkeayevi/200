# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 18:47:48 2019

@author: BerkeAyevi
"""

import math as m

vel=int(input("Initial Velocity (m/s): "))
angle=int(input("Angle (deg): "))

mass= (1.000) #in kg
dt = (0.001) #time step
g = (9.80665) #m/s^2 g 
dcof= (0.005) #drag coefficent of sphere Cd (unitless)
def d2r(x):# degree to radians
    rad= m.radians(x)
    return rad
    
Fd = vel*vel*dcof #drag force
t = [0]
x=[0]
z=[0]
vx=[vel*m.cos(d2r(angle))] #Vx  component
vz=[vel*m.sin(d2r(angle))] #Vz component
ax=[-(Fd*m.cos(d2r(angle)))/mass]
az=[-g-(Fd*m.sin(d2r(angle)))/mass] 
i= 0   
while (z[i] >= 0):
    t.append(t[i]+dt)                
    
    vx.append(vx[i]+dt*ax[i])  # Update the velocity
    vz.append(vz[i]+dt*az[i])

    x.append(x[i]+dt*vx[i])    # Update position
    z.append(z[i]+dt*vz[i])    
    
    vel = m.sqrt(vx[i+1]**2 + vz[i+1]**2)   # magnitude of velocity
    Fd = vel*vel*dcof
    ax.append(-(Fd*m.cos(d2r(angle)))/mass)     
    az.append(-g-(Fd*m.sin(d2r(angle))/mass))
    
    i = i +1

f = open("S22.dat","w")
ran=len(t)
for i in range(0,ran):
    f.write("{0:8.5f}\t{1:8.5f}\t{2:8.5f}\n".format(t[i],x[i],z[i]))
f.close()
   