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
    l = 110 - x
    return l


def theta(x):
    l = length(x)
    theta = np.arccos((a**2 + l**2 - c**2)/(2*a*l))
    return theta


def phi(x):
    l = length(x)
    phi = np.arccos((a**2 - l**2 + c**2)/(2*a*c))
    # print((phi*180)/np.pi)
    return phi


x_vals = np.linspace(0, 35, 36)
l_vals = []
t_vals = []
p_vals = []

# Range of angles and lengths
for i in range(0, len(x_vals)):
    x = x_vals[i]
    l_vals.append(length(x))
    t_vals.append((theta(x)*180)/math.pi)
    p_vals.append((phi(x)*180)/math.pi)
    # if (i==0):
    #     print(p_vals)

# Force relationship between spring and gravity

tr_vals = []
pr_vals = []

# Range of angles and lengths for calculation
for i in range(0, len(x_vals)):
    x = x_vals[i]
    tr_vals.append(theta(x))
    pr_vals.append(phi(x))



def spring_f(phi, theta):
    # 0.5 is added since there are 2 springs
	# orginal ratio : (92.5/46.2)
	# alternate ratio : (46.2/92.5)
    fs = ((fg*np.sin(phi+(np.pi/2)))/np.sin(theta)*(46.2/92.5))*0.5
    return fs


spring_force = []

for i in range(0, len(t_vals)):
    phi = pr_vals[i]
    theta = tr_vals[i]
    spring_force.append(spring_f(phi, theta))

figure, axis = plt.subplots(3, 2)

offset_from_wheel = []

for i in range(0,len(p_vals)):
    offset_from_wheel.append(92.5*np.cos(pr_vals[i])-70)
    

spring_const = []
spring_count = []

for i in range(1,len(x_vals)):
    spring_count.append(x_vals[i])
    spring_const.append(spring_force[i]/(x_vals[i]*10**(-3)))

# spring average between 15mm compression and 35mm compression
k_sum = 0
n = 0 
for i in range(15,34):
    k_sum += spring_const[i]
    n +=1
k_avg = k_sum/n

print(f"Average Value of k from 15 to 34mm of compression: {k_avg}")

axis[0, 0].scatter(x_vals,l_vals, color="black", marker="*")
axis[0,0].set_xlabel("Spring Compression (mm)")
axis[0, 0].set_ylabel("Length of Spring")

axis[0, 1].scatter(x_vals, p_vals, color="blue", marker="*")
axis[0, 1].set_xlabel("Spring Compression (mm)")
axis[0, 1].set_ylabel("Phi Angle Between x-axis and Beam")

axis[1, 0].scatter(x_vals, t_vals, color="red", marker="*")
axis[1, 0].set_xlabel("Spring Compression (mm)")
axis[1, 0].set_ylabel("Theta Angle Between Spring Force and Beam")

axis[1, 1].scatter(x_vals, spring_force, color="purple", marker="*")
axis[1, 1].set_xlabel("Spring Compression (mm)")
axis[1, 1].set_ylabel("Total Force required of Spring")

axis[2, 0].scatter(x_vals, offset_from_wheel, color="purple", marker="*")
axis[2, 0].set_xlabel("Spring Compression (mm)")
axis[2, 0].set_ylabel("Distance to edge of wheel")

axis[2, 1].scatter(spring_count, spring_const, color="purple", marker="*")
axis[2, 1].set_xlabel("Spring Compression (mm)")
axis[2, 1].set_ylabel("Estimated Spring Constant(N/m)")

plt.show()
