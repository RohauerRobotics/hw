import control as ct
import numpy as np
import matplotlib.pyplot as plt

C = 9.99*10**(-6) # capacitance
R = 10.96*10**(3)

sys = ct.tf(1,[C*R,1])
[mag, phase, w] = ct.bode(sys,plot=False)

w_b = 1/(C*R)
print(f"w_b = {w_b}")

tested_w = [w_b*10**(-1), w_b*10**(-0.5), w_b*10**(0),
            w_b*10**(0.25), w_b*10**(0.5), w_b*10**(0.75), w_b*10**(1)]
print(tested_w)
measured_mag = [0.9868, 0.9481, 0.703, 0.4924, 0.3026, 0.1778, 0.1006]
plt.scatter(tested_w, measured_mag, label="Measured Magnitudes")

w_y = np.linspace(0,1,100)
w_x = (1/(C*R))*np.ones(len(w_y))
plt.loglog(w_x, w_y, label="Bandwidth Frequency")
plt.loglog(w,mag, label="Expected Behavior")
plt.grid(True, which="both", ls="-", color='0.65')
plt.legend(loc="upper right")
plt.ylabel("Magnitude")
plt.xlabel("Frequency(w)")
plt.title("Expected vs Measured Magnitudes of Signals into Low Pass Filter")
plt.show()