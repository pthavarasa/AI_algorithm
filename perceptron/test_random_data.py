import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from random import shuffle
from perceptron import Perceptron

centre1=np.array([3,3])
centre2=np.array([-3,-3])
sigma1=np.array([[1.5,0],[0,1.5]])
sigma2=np.array([[1.5,0],[0,1.5]])
taille1=200
taille2=200
cluster1=np.random.multivariate_normal(centre1,sigma1,taille1)
cluster2=np.random.multivariate_normal(centre2,sigma2,taille2)

plt.scatter([point[0] for point in cluster1], [point[1] for point in cluster1], color="pink")
plt.scatter([point[0] for point in cluster2], [point[1] for point in cluster2], color="blue")
plt.scatter(centre1[0], centre1[1], color="red")
plt.scatter(centre2[0], centre2[1], color="red")

#plt.show()

DEBUG = False

# convert data to [x, y, label] and [ shuffle (just for testing) ]
data = []
for i in cluster1:
	data.append([i[0], i[1], 1])
for i in cluster2:
	data.append([i[0], i[1], 0])
shuffle(data)

# init 
e = 0.1
p = Perceptron(data, e)

# n training iteration 
n = 10
for i in range(0,n):
	if DEBUG: print(p.get_weigth())
	p.learn()

# check all data's expected label and predicted label
error = 0
wl = p.get_weigth_lenth()
for d in data:
	predicted = p.decision(d)
	if predicted != d[wl-1]:
		error+=1
		print("Error prediction : Expected '{}' Predicted '{}' at '{}'".format(d[wl-1], predicted, data.index(d)))
	if DEBUG:
		print("excepted  : " + str(d[wl-1]))
		print("predicted : " + str(predicted))
		print("")
		
print("Test passed with {}% error rate.".format(100*error/len(data)))

