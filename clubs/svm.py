import matplotlib.pyplot as plt
import numpy as np

# Make array of data to be separated by a SVM (y,x_1,x_2)
num_data = 100 
half = int(num_data*0.5)

x_1 = np.append(np.random.uniform(0, 4, size=(half, 1)),
                np.random.uniform(2, 8, size=(half, 1)))
x_1 = x_1[:,np.newaxis]
x_2 = np.append(np.random.uniform(0, 4, size=(half, 1)),
                np.random.uniform(10, 15, size=(half, 1)))
x_2 = x_2[:, np.newaxis]
values = np.append(np.ones(half)*-1,np.ones(half))

values = values[:,np.newaxis]
values = np.append(values, x_1,1)
values = np.append(values, x_2, 1)

# print(np.matrix(values))
# print(values[0:-1,0])
# print(values[0:-1,1])
# print(values[0:-1,2])
b = np.ones(num_data)
b = b[:,np.newaxis]

x = np.append(x_1, x_2, 1)
# x = np.append(x, x_2, 1)

print(np.matrix(x))
# print(f"X length = {len(x[0])}")

def svm_function(x,y):
	# init weights
	print(len(x[0]))
	w = np.zeros(len(x[0]))

	# init learning rate
	l_rate = 1 

	# epoch
	epoch = 1000

	# begin training
	for e in range(epoch):
		for i, val in enumerate(x):
			val1 = np.dot(x[i,:],w)
			if (y[i]*val1 < 1):
				w = w + l_rate*((y[i]*x[i,:]) - (2*(1/epoch)*w))
			else:
				w = w + l_rate*(- (2*(1/epoch)*w))
	
	print("Training done!")

	return w

b,w = svm_function(x,values[:,0])
print(w)
plot_x_1 = np.linspace(min(values[:,1]),max(values[:,1]), 1000)
plot_x_2 = np.linspace(min(values[:, 2]), max(values[:, 2]), 1000)
figure, axis = plt.subplots(2, 2) 

axis[0, 0].scatter(values[0:half, 1], values[0:half, 2], color="red", marker="*")
axis[0, 0].scatter(values[half:-1, 1], values[half:-1, 2],
                   color="blue", marker="^")
axis[0,0].plot(plot_x_1, plot_x_1*w)
axis[0,0].set_xlabel("x_1")
axis[0, 0].set_ylabel("x_2")
axis[0, 0].set_title("Original Data")

axis[0, 1].scatter(values[0:half, 2], values[0:half, 1], color="red", marker="*")
axis[0, 1].scatter(values[half:-1, 2], values[half:-1, 1],
                   color="blue", marker="^")
axis[0, 1].set_xlabel("x_2")
axis[0, 1].set_ylabel("x_1")
axis[0, 1].set_title("Original Data")

axis[1, 0].scatter(values[0:-1, 1], values[0:-1, 0],color="black")
# axis[1, 0].plot(plot_x_1, plot_x_1*w[0]+ plot_x_1*w[1]+ b)
axis[1, 0].set_title("x_1 vs Output Value")
axis[1, 0].set_xlabel("x_1")
axis[1, 0].set_ylabel("output value")
# axis[1,0].set_ylim(-1.5,1.5)

axis[1, 1].scatter(values[0:-1, 2], values[0:-1, 0], color="black")
axis[1, 1].set_title("x_1 vs Output Value")
axis[1, 1].set_xlabel("x_1")
axis[1, 1].set_ylabel("output value")
axis[1, 1].set_ylim(-1.5, 1.5)


plt.show()
