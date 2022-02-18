# program for graphing cooling curve for nitrobenzene and nitrobenzene + an unknown solution
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

times = [0,0.5,1,1.5,2,2.5,]
for x in range(3,17):
    times.append(x)

# print(len(times))

nitro_pure = [12.5,10.75,8.75,6.50,4.8,4.5,4.25,4.5,5,5.3,5.3,5.3,5.3,5.3,5.2,5.2,5.2,5.2,5.2,5.2]

nitro_unk = [9,8,7,5,3.75,3,1.25,-1.25,-2.25,-2.5,-2.25,-1.8,-1.5,-1.6,-1.75,-1.8,-1.9,-2,-2.1,-2.2]

font = {'family' : 'Times New Roman',
        'weight' : 'normal',
        'size'   : 22}

matplotlib.rc('font', **font)

xvals2 = np.linspace(0,16.25,1000)

def make_line(limit1, limit2, list):
    coef, intercept = np.polyfit(times[limit1:limit2],list[limit1:limit2],1)
    #print(list[limit1:limit2])
    coefs = np.polyfit(times[limit1:limit2],list[limit1:limit2],1)
    poly1d_fn = np.poly1d(coefs)
    return poly1d_fn

line1 = make_line(0,5, nitro_pure)
line2 = make_line(5,20, nitro_pure)
line3 = make_line(0,8, nitro_unk)
line4 = make_line(8,20, nitro_unk)

pure_point = []
unk_point = 0

pure_count = 0
for x in range(0,50):
    w = line1(x*0.1)
    q = line2(x*0.1)
    if ((abs(w-q))<0.05):
        pure_point = line1(x*0.1)
        break
    else:
        pass

for x in range(0,50):
    w = line3(x*0.1)
    q = line4(x*0.1)
    if (abs(abs(w)-abs(q))<0.045):
        unk_point= line1(x*0.1)
        break
    else:
        pass

print("Freezing Point of Pure", pure_point)
print("Freezing Point of Unknown", unk_point)

plt.scatter(times, nitro_pure, c='#12861E', marker='o', label ="Pure Nitrobenzene")
plt.scatter(times, nitro_unk, c='#5900C1', marker='X', label ="Nitrobenzene + Unknown")
plt.plot(xvals2,line1(xvals2), c='#12861E')
plt.plot(xvals2,line2(xvals2), c='#12861E')
plt.plot(xvals2,line3(xvals2), c='#5900C1')
plt.plot(xvals2,line4(xvals2), c='#5900C1')
#plt.scatter(xvals1, yvals2, c='#34eb74')
#plt.xlim(0,0.5)
#plt.ylim(0,2.5)
plt.title(r'Freezing Point of Nitrobenzene vs Nitrobenzene with Unknown Solute')
plt.xlabel(r'Time(min)')
plt.ylabel('Temp C'+ chr(176))
plt.legend(loc="upper right")
plt.ylim(0,16.25)
plt.ylim(-5,13.5)
# Show the boundary between the regions:
#theta = np.arange(0, np.pi / 2, 0.01)
#plt.plot(r0 * np.cos(theta), r0 * np.sin(theta))

plt.show()
