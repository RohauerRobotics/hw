import numpy as np
import matplotlib.pyplot as plt
import control as ct

t = np.linspace(0,5,200)
u = np.random.random(len(t)) + np.sin(2*t)
filter = ct.tf(1,[0.1,1])
print(filter)
filter2 = ct.tf(1, [1,1])
print(filter2)

t, y = ct.forced_response(filter,t,u)
t, y2 = ct.forced_response(filter2, t,u)

plt.plot(t,u,"C1",t,y,"k",t,y2,"C0")
plt.legend(("Input u", "Output for Tau = 0.1", "Output y2 for Tau = 1"))
plt.xlabel("Time (sec)")
plt.ylabel("System Response")
plt.show()

ct.bode_plot(filter,omega_limits=(0.1,100),color='k',label="Tau 0.1")
ct.bode_plot(filter2, omega_limits=(0.1, 100), color='C0', label="Tau 1")
plt.legend()
plt.show()