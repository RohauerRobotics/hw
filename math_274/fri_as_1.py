# Friday Assignment #1

import numpy as np
import matplotlib as mpl
import math

# program variables
h = 0.1
xn = 1
x0 = 0

# Euler's Method

def slope_function(x,y):
    ret = ((x**3)*math.e**(-2*x))-(2*y)
    return ret

steps = int(xn/h)
print("number of steps:" , steps)

xvals = [x0]
for i in range(1, steps + 1):

    xvals.append(round(x0 + (i*h), 5))

print(xvals)

y_pred = []
for i range(1, steps + 1):
