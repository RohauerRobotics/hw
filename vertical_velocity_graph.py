import matplotlib.pyplot as plt
import numpy as np

import matplotlib
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 22}

matplotlib.rc('font', **font)

time = np.linspace(0,1.25,1000)
position = 5 - 9.8*time

plt.plot(time, position)
plt.title('Vertical Velocity vs Time')
plt.xlabel('Time(seconds)')
plt.ylabel('Approximate Vertical Velocity(meters/second)')
plt.ylim([-5.78,6])
plt.show()
