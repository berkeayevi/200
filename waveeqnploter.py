import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.style.use('dark_background')

fig = plt.figure()
fig.set_dpi(100)
ax1 = fig.add_subplot(1,1,1)


c = 1 #speed of wave
x0 = np.linspace(-pi,pi,10000) #x axis
t0 = 0 #Initial time
dt = 0.05#delta t

def u(x,t): #equation
    return 5*(np.sin((2*(x)^2)-(3(t)^2))

a = array([])

for i in range(500)
    value = u(x0,t0)
    t0 = t0 + dt
    a.append(value)

    k = 0
def animate(i):
    global k
    x = a[k]
    k += 1
    ax1.clear()
    plt.plot(x0,x,color='cyan')
    plt.grid(True)
    plt.ylim([-2,2])
    plt.xlim([-pi,pi])
    
anim = animation.FuncAnimation(fig,animate,frames=360,interval=20)
plt.show()
