import numpy as np
import matplotlib.pyplot as plt
import control as ct

# First order low-pass filter of type
# 1/(tau)*s+a , where tau = 0.1 and a = 1

# tf takes (numerator coefficients, denominator coefficients)
R = 100 
C = 2 
# second_order_filter = ct.tf([1,0,0], [1, 2/(R*C),1/(R**2*C**2)])
second_order_filter = ct.tf([R**2*C**2, 0, 0], [R**2*C**2, 2*R*C, 1])
print(second_order_filter)
mag, phase, omega = ct.bode(second_order_filter)
plt.show()
