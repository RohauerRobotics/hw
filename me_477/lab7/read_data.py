import scipy.io
import numpy as np
import matplotlib.pyplot as plt

# Load the data from the .mat file
# all_data = scipy.io.loadmat("AppliedTorque-2.mat")
all_data = scipy.io.loadmat("StepChange.mat")

dt = 0.005  # Time step in seconds

# Convert the loaded arrays into 1D arrays (flatten them)
vel_data = all_data['Velocity'].flatten()
output_data = all_data['Output'].flatten()

# Create the time vector based on the data length and time step
time = np.arange(0, dt * len(vel_data), dt)

# Create two subplots, one above the other, sharing the same x-axis
fig, axs = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Top subplot: Voltage data
axs[0].plot(time, output_data, label="Analog Output Data", color='blue')
axs[0].set_ylabel("Measured Voltage (V)")
axs[0].set_title("Motor Voltage vs Time")
axs[0].legend(loc="upper right")

# Bottom subplot: Speed data
axs[1].plot(time, vel_data, label="Motor Angular Velocity Data", color='red')
axs[1].set_xlabel("Time (s)")
axs[1].set_ylabel("Angular Velocity")
axs[1].set_title("Motor Speed vs Time")
axs[1].legend(loc="upper right")

plt.tight_layout()
plt.show()
