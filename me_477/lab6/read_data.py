import scipy.io
import numpy as np
import matplotlib.pyplot as plt

all_data =  scipy.io.loadmat("Sine_200Hz.mat")
# print(data)

dt = 0.0005 # time in seconds

input_data = all_data['Input'].tolist()
output_data = all_data['Output'].tolist()

# filt_data = []
# for i in range(1,len(data)):
#     if (data[i][0]>0):
#         filt_data.append(data[i][0])
#     else: 
#         pass

time = np.arange(0,(dt)*len(input_data),(dt))

plt.plot(time, input_data,label="Input Data")
plt.plot(time, output_data,label="Output Data")
plt.xlabel("Time(s)")
plt.ylabel("Measured Voltage(V)")
plt.title("Input and Output Data for 8Hz Square Wave Input")
plt.legend(loc="upper right")
plt.show()