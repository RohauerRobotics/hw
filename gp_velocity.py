# projectile Velocity

import matplotlib.pyplot as plt
import numpy as np

import matplotlib
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 22}

matplotlib.rc('font', **font)

time = np.linspace(0,0.75,1000)
position = np.linspace(1.33,1.33,1000)

plt.plot(time, position)
plt.title('Horizontal Velocity vs Time')
plt.xlabel('Time(seconds)')
plt.ylabel('Approximate Horizontal Velocity(meters/second)')
plt.ylim([0,2])
plt.show()

time1 = np.linspace(0,0.75,1000)
position1 = time*0

plt.plot(time1, position1)
plt.title('Vertical Velocity vs Time')
plt.xlabel('Time(seconds)')
plt.ylabel('Approximate Vertical Velocity(meters/second)')
plt.ylim([-1,1])
plt.show()
