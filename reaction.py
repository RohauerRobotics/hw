# chem hw graph for Reaction Rate Lab
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

ln_k = [-9.41, -9.89, -9.61]

inverse_temp = [0.00339, 0.00327, 0.00355]

font = {'family' : 'Times New Roman',
        'weight' : 'normal',
        'size'   : 22}

matplotlib.rc('font', **font)

xvals1 = []
yvals1 = []


coef = np.polyfit(inverse_temp,ln_k,1)
poly1d_fn = np.poly1d(coef)

xvals2 = np.linspace(0,0.005,100)
plt.scatter(inverse_temp, ln_k, c='#eb34db')
plt.plot(xvals2,poly1d_fn(xvals2), c='#eb34db', label = 'y='+str(round(poly1d_fn(1),2))+' (Ea/R) '+str(round(poly1d_fn(0),2)))
plt.legend(loc="upper right")
#plt.scatter(xvals1, yvals2, c='#34eb74')
plt.xlim(0,0.005)
plt.ylim(-10,2.5)
plt.title('Natural Log K vs 1/T')
plt.xlabel('1/T')
plt.ylabel('ln(k)')

#plt.ylim()
#plt.ylim()
# Show the boundary between the regions:
#theta = np.arange(0, np.pi / 2, 0.01)
#plt.plot(r0 * np.cos(theta), r0 * np.sin(theta))

plt.show()
