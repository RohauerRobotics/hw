import matplotlib.pyplot as plt
import numpy as np
import matplotlib
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 22}

matplotlib.rc('font', **font)

time = np.linspace(0,1.25,1000)
position = time*1.2
plt.plot(time, position)
plt.title('Horizontal Position vs Time')
plt.xlabel('Time(seconds)')
plt.ylabel('Approximate Horizontal Position(meters)')
plt.show()
