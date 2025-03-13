import numpy as np
import matplotlib.pyplot as plt
import control as ct

# define constants
w_n = 2*np.pi*40
z = 0.5

# Define the transfer function
num = [w_n**3]
den = [1,(2*z*w_n)+(w_n),(w_n**2)+(2*z*w_n**2), w_n**3]  # Represents s + 1
sys = ct.tf(num, den)
print(sys)
# Generate the Bode plot
omega = np.logspace(-1, 4, 1000)  # Frequency range
mag, phase, om = ct.bode_plot(sys, omega, plot=True)

# Customize the plot (optional)
plt.title('Bode Plot')
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Magnitude (dB) / Phase (degrees)')
plt.grid(True)
plt.show()