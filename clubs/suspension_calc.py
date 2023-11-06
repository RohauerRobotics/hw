# this is a file for finding the range of suspension and the forces of it
import numpy as np
import matplotlib.pyplot as plt
import math

# define motion of rod
# Phi is the angle between the spring force and the end of the pivoting beam
# Theta is the angle between the pivoting beam and the x axis

# Estimations
# Force of gravity : ~140N (30 lbs) for the whole build so 35N per wheel of reactive force from gravity

# Phi, theta, and the spring force are functions of the displacement of the spring

#global constants

# a is the total length of the pivoting beam (mm)
a = 138.688

# c is the length of the x distance between the center of the wheel and the lower end of the spring (mm)
c = 145

# force of gravity (N)
fg = 35

def length(x):
    l = 110 -x
    return l

def theta(x):
    l = length(x)
    theta = np.arccos((a**2 + l**2 -c**2)/(2*a*l))
    return theta

def phi(x):
    l = length(x)
    phi = np.arccos((a**2 - l**2 + c**2)/(2*a*c))
    print((phi*180)/np.pi)
    return phi


x_vals = np.linspace(0,35, 36)
l_vals = []
t_vals = []
p_vals = []

# Range of angles and lengths
for i in range(0, len(x_vals)):
    x = x_vals[i]
    l_vals.append(length(x))
    t_vals.append((theta(x)*180)/math.pi)
    p_vals.append((phi(x)*180)/math.pi)

# Force relationship between spring and gravity
def spring_f(phi, theta):
    fs = (fg*np.sin(phi+(np.pi/2)))/np.sin(theta)*(92.5/46.2)
    return fs

spring_force = []

for i in range(0, len(t_vals)):
    phi = p_vals[i]
    theta = t_vals[i]
    spring_force.append(spring_f(phi,theta))


# plt.scatter(x_vals, l_vals, color="black", label="Lengths")
# plt.scatter(x_vals, p_vals, color="red", label="Phi")
# plt.scatter(x_vals, t_vals, color="green", label="Theta")
plt.scatter(x_vals, spring_force)
plt.legend()
plt.show()

    