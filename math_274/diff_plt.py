import numpy as np
import matplotlib.pyplot as plt

nx, ny = 0.5, 0.5
x = np.arange(-10, 10, nx)
y = np.arange(-10, 25, ny, step=2)

X, Y = np.meshgrid(x,y)

dy = 14*Y**2 + 5*Y**3 - Y**4
dx = np.ones(dy.shape)

a = 50

dyu = dy/np.sqrt(dy**2 + dx**2)*a
print(f"DYU: \n {dyu}")
dyx = dx/np.sqrt(dy**2 + dx**2)*a
print(f"DYX: \n {dyx}")

plt.quiver(X, Y, dyx, dyu, color="purple")
plt.title("Normalized Direction Field")
plt.show()
