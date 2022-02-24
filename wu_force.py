# incline plane graphs
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

angles  = [1.491,
1.834,
2.148,
2.443,
2.541,
2.835,
3.090,
3.335]

efficiency = [46.0, 48.0, 52.0, 57.5, 62.1, 65.7, 67.3, 67.2]

font = {'family' : 'Times New Roman',
        'weight' : 'normal',
        'size'   : 22}

matplotlib.rc('font', **font)

xvals1 = []
yvals1 = []

# coef, intercept = np.polyfit(xvals1,yvals1,1)
# coefs = np.polyfit(xvals1,yvals1,1)
# poly1d_fn = np.poly1d(coefs)
#
# xvals2 = np.linspace(0,13,1000)
plt.scatter(angles, efficiency, c='#000000')
# plt.plot(xvals2,poly1d_fn(xvals2), c='#eb34db', label = 'y='+str(round(coef,3))+'x'+str(round(intercept,3)))
# plt.legend(loc="upper left")
#plt.scatter(xvals1, yvals2, c='#34eb74')
#plt.xlim(0,0.5)
#plt.ylim(0,2.5)
plt.title('Wheels Up\nGraph of Work Efficiency vs Applied Force')
plt.xlabel(r'Applied Force (N)')
plt.ylabel('Work Efficiency %')

plt.xlim(0, 4)
plt.ylim(0, 72.5)

# Show the boundary between the regions:
#theta = np.arange(0, np.pi / 2, 0.01)
#plt.plot(r0 * np.cos(theta), r0 * np.sin(theta))

plt.show()
