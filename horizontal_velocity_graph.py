import matplotlib.pyplot as plt
import numpy as np

import matplotlib
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 22}

matplotlib.rc('font', **font)
time = np.linspace(0,1.25,1000)
position = np.linspace(1.2,1.2,1000)

plt.plot(time, position)
plt.title('Horizontal Velocity vs Time')
plt.xlabel('Time(seconds)')
plt.ylabel('Approximate Horizontal Velocity(meters/second)')
plt.ylim([0,2.5])
plt.show()
