# linear regression with matricies
import numpy as np
from matplotlib import pyplot as plt

# define linear space to plot y values --> (100,1) column vector 
x_show = np.linspace(-10,100,100)
x_show = x_show[:,np.newaxis]

# define random slope between -1 and 1
m = np.random.uniform(-1, 1, size=(1,1))
# define random offset values
off = np.random.uniform(-5,5,size=(100,1))

y = x_show*m + off
print(x_show.shape)
print(off.shape)
print(y.shape)

# define function
# f(x) = x^(T)w

# add b vector representing offset in (num_samples,1) column vector
b = np.ones(100)
b = b[:,np.newaxis]
print(b.shape)

# append b vector to fist column before x --> (100,2) matrix
x = np.append(b,x_show,1)
print(x.shape)

# apply function minimization W = (X(T)*X)^-1*X(T)*Y --> (2,1) row matrix
w = np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(x),x)),np.transpose(x)),y)
print(w.shape)
print(w[0,0])
print(w[1,0])

plt.scatter(x_show,y)
plt.plot(x,w[1,0]*x+w[0,0])
plt.show()
