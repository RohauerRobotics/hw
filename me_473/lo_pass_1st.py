import numpy as np
import matplotlib.pyplot as plt
import control as ct

# First order low-pass filter of type
# 1/(tau)*s+a , where tau = 0.1 and a = 1
 
# tf takes (numerator coefficients, denominator coefficients)
lo_pass_filter = ct.tf(1,[0.1,1])
print(lo_pass_filter)
mag, phase, omega =  ct.bode(lo_pass_filter)
plt.show()

# Customize the plot
plt.figure()
plt.subplot(2, 1, 1)
plt.semilogx(omega, mag)  # Bode magnitude plot
plt.title("Bode Plot")
plt.grid(True)
plt.ylabel("Magnitude (dB)")

plt.subplot(2, 1, 2)
plt.semilogx(omega, phase)  # Bode phase plot
plt.grid(True)
plt.xlabel("Frequency (rad/s)")
plt.ylabel("Phase (deg)")
plt.show()

plt.figure()
t = np.linspace(0,5,200) # timespan
u = np.sin(t) # input function
plt.plot(t,u, label="Input Function")

t_o,y = ct.forced_response(lo_pass_filter,t,u)
plt.plot(t_o, y, label="Output Function")
plt.grid()
plt.legend(loc="upper right")
plt.show()