import matplotlib.pyplot as plt
import matplotlib
import numpy as np

deg3 = [2.9,11.8,5.1,0.8603,0.8273]
deg5 = [3.3,14.6,6.5,1.119,1.083]
deg8 = [3.4,15.6,7,1.128,1.1]
deg10 = [3.8,19.6,9.1,1.52,1.476]
deg12 = [4,27.1,13.4,2.261,2.131]

full_list = [deg3,deg5,deg8,deg10,deg12]

font = {'family' : 'Times New Roman',
        'weight' : 'normal',
        'size'   : 22}

matplotlib.rc('font', **font)

xvals1 = []
yvals1 = []

for x in range(0, len(full_list)):
    xvals1.append(np.sin(np.radians(full_list[x][2])))

for y in range(0, len(full_list)):
    yvals1.append(full_list[y][4])

#yvals2 = []

for y in range(0, len(full_list)):
    yvals1.append(full_list[y][3])

for x in range(0, len(full_list)):
    xvals1.append(np.sin(np.radians(full_list[x][2])))


coef = np.polyfit(xvals1,yvals1,1)
poly1d_fn = np.poly1d(coef)

xvals2 = np.linspace(0,0.5,100)
plt.scatter(xvals1, yvals1, c='#eb34db')
plt.plot(xvals2,poly1d_fn(xvals2), c='#eb34db', label = 'y='+str(round(poly1d_fn(1),4))+r'(sin${\theta}$)'+str(round(poly1d_fn(0),4)))
plt.legend(loc="upper right")
#plt.scatter(xvals1, yvals2, c='#34eb74')
plt.xlim(0,0.5)
plt.ylim(0,2.5)
plt.title(r'Sine of ${\theta}$ vs Acceleration')
plt.xlabel(r'Sine of ${\theta}$')
plt.ylabel('Acceleration (m/sec$^2$)')

#plt.ylim()
#plt.ylim()
# Show the boundary between the regions:
#theta = np.arange(0, np.pi / 2, 0.01)
#plt.plot(r0 * np.cos(theta), r0 * np.sin(theta))

plt.show()
