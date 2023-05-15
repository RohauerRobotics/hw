# Principal Component Analysis Test
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# Create Random 3D Data
data = np.random.rand(3,20)
# print(np.matrix(data))

# get row average for each dimension
mean = np.mean(data, axis=1)
print("Mean: \n", mean)
center_data = data - mean

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(data[0,:], data[1,:], data[2,:])
ax.scatter3D(mean[0], mean[1], mean[2], color="red")
ax.scatter3D(center_data[0,:],center_data[1,:],center_data[2,:])
plt.show()
