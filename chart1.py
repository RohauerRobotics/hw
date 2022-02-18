import matplotlib.pyplot as plt
import matplotlib
import numpy as np

data  = [1,0.25,1.686,4.1385,1.487,1.279,0.359,0.309,1.579,1.036,0.382,0.250,
2,0.35,1.686,5.1195,2.437,1.637,0.476,0.320,2.088,1.467,0.408,0.287,
3,0.45,1.686,6.1005,3.025,2.216,0.496,0.363,2.67,1.572,0.438,0.258,
4,0.55,1.686,7.0815,3.454,2.459,0.488,0.347,2.75,1.89,0.388,0.267,
5,0.65,1.686,8.0625,3.951,2.924,0.490,0.363,3.424,2.078,0.425,0.258,
6,0.75,1.686,9.0435,5.188,3.534,0.574,0.391,4.22,2.6,0.467,0.287,
7,0.85,1.686,10.0245,5.268,3.775,0.526,0.377,4.03,2.488,0.402,0.248,
8,0.95,1.686,11.0055,6.898,5.02,0.627,0.456,5.403,3.255,0.491,0.296,
9,1.05,1.686,11.9865,6.444,5.01,0.538,0.418,5.74,3.661,0.479,0.305,
10,1.15,1.686,12.9675,6.873,5.322,0.530,0.410,6.444,3.92,0.497,0.302]

font = {'family' : 'Times New Roman',
        'weight' : 'normal',
        'size'   : 22}

matplotlib.rc('font', **font)

xvals1 = []
yvals1 = []

for x in range(0, 10):
    xvals1.append(data[3+(x*12)])

print("total force:", xvals1)

for y in range(0, 10):
    yvals1.append(data[5+(y*12)])

print("total force:", yvals1)
#yvals2 = []

coef, intercept = np.polyfit(xvals1,yvals1,1)
coefs = np.polyfit(xvals1,yvals1,1)
poly1d_fn = np.poly1d(coefs)

xvals2 = np.linspace(0,13,1000)
plt.scatter(xvals1, yvals1, c='#eb34db')
plt.plot(xvals2,poly1d_fn(xvals2), c='#eb34db', label = 'y='+str(round(coef,3))+'x'+str(round(intercept,3)))
plt.legend(loc="upper left")
#plt.scatter(xvals1, yvals2, c='#34eb74')
#plt.xlim(0,0.5)
#plt.ylim(0,2.5)
plt.title(r'Feet Down Kinetic Friction vs Normal Force')
plt.xlabel(r'Total Normal Force(N)')
plt.ylabel('Kinetic Friction(N)')

plt.ylim(0,13.25)
plt.ylim(0,7.25)
# Show the boundary between the regions:
#theta = np.arange(0, np.pi / 2, 0.01)
#plt.plot(r0 * np.cos(theta), r0 * np.sin(theta))

plt.show()
