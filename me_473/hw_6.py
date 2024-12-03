# Plot of various resistance ratios
import numpy as np
import matplotlib.pyplot as plt

rl_rc = [0.1,1,10]

# v0_vref = np.linspace(0,1,100)
# theta_theta_max =  np.array(np.linspace(0,1,100))
theta = []
for i in range(0,100):
	theta.append(i/100)
print(theta[1])
def v0_over_vref(theta_over_theta_max, rl_over_rc):
	v = (theta_over_theta_max*rl_over_rc)/(rl_over_rc+theta_over_theta_max-(theta_over_theta_max)**2)
	return v

def err(v,th):
	e = (abs(v-th)/th)*100
	return e


labels = ["R_L/R_C=0.1", "R_L/R_C=1.0", "R_L/R_C=10"]
for i in range(0,len(rl_rc)):
	r = rl_rc[i]
	error_list = []
	v_list = []
	for n in range(1,len(theta)):
		v = v0_over_vref(theta[n],r)
		v_list.append(v)
		e = err(v, theta[n])
		error_list.append(e)
	# plt.plot(theta[1:],v_list)
	plt.plot(theta[1:], error_list,label=labels[i])

plt.legend(loc="upper right")
plt.xlabel("Theta/Theta Max")
plt.ylabel("Absolute Percent Error")
plt.title("Potentiometer Electrical Nonlinearity Error")
plt.show()