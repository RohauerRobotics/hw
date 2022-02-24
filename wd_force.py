# incline plane graphs
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

angles  = [0.903,
1.197,
1.550,
1.844,
2.040,
2.433,
2.639,
2.874]

efficiency = [93.1,
90.1,
88.4,
93.3,
94.7,
93.9,
96.6,
95.6]

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
plt.title('Wheels Down\nGraph of Work Efficiency vs Applied Force')
plt.xlabel(r'Applied Force (N)')
plt.ylabel('Work Efficiency %')

plt.xlim(0, 4)
plt.ylim(0, 100)

# Show the boundary between the regions:
#theta = np.arange(0, np.pi / 2, 0.01)
#plt.plot(r0 * np.cos(theta), r0 * np.sin(theta))

plt.show()
