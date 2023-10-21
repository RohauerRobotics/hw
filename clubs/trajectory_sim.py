# simulation for estimating initial velocity of a small object travelling about 15.24m
import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
# ball properties

# 1mm diameter
radius = 0.0005 

mass = 0.0011

# velocity in m/s (x,y)
r0 = [0,0]
v0 = [10, 10]
def mag(x): 
    return math.sqrt(sum(i**2 for i in x))

def velocity(v,v0,t):
	v = v0 + [-0.5*1.2*np.pi*radius**2*0.47 *
           mag(v)*(v[0]/mag(v)), -9.81*t - 0.5*1.2*np.pi*radius**2*0.47*mag(v)*(v[1]/mag(v))]
	return v

x = range(0,2,1000)
vx = []
vy = [] 
v = v0
for i in x:
    v1 = velocity(v,v0,i)
    vx = v1[0]
    vy = v1[1]
    v = v1

plt.scatter(x,vy, c="blue")
plt.scatter(x,vy, color="black")

plt.title('Velocity graphs')
plt.xlabel('Time(t)')
plt.ylabel('Velocity(m/s)')

plt.show()