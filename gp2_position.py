# ball rolling graphs
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 22}

matplotlib.rc('font', **font)

time = np.linspace(0,0.5,1000)
position = 1.333*time
horizontal_position = [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]

plt.plot(time, position)
plt.title('Horizontal Position vs Time')
plt.xlabel('Time(seconds)')
plt.ylabel('Approximate Horizontal Position(meters)')
#plt.ylim([0,2.5])
plt.show()

time1 = np.linspace(0,0.5,1000)
position1 = -4.9*time**2
horizontal_position = [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]

plt.plot(time1, position1)
plt.title('Vertical Position vs Time')
plt.xlabel('Time(seconds)')
plt.ylabel('Approximate Vertical Position(meters)')
plt.ylim([-1,.5])
plt.show()
