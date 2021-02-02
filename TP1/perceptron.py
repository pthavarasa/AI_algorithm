import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

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



#print(cluster1)
#print(cluster2)


class Perceptron:
	def __init__(self, data, e):
		self.weigth_lenth = len(data[0])
		self.epsilon = e
		self.weigth = []
		self.weigth_init()
		self.data = data

	def weigth_init(self):
		for i in range(0, self.weigth_lenth):
			self.weigth.append(random.randint(-1,1))
		return self.weigth

	def decision(self, x):
		s = self.weigth[self.weigth_lenth - 1]
		for i in range(0, self.weigth_lenth - 1):
			s += self.weigth[i] * x[i]
		return 1 if s >= 0 else -1

	def learn(self):
		for e in self.data:
			d = self.decision(e)
			er = e[self.weigth_lenth - 1] - d
			self.weigth[self.weigth_lenth - 1] += er * self.epsilon
			for i in range(0, self.weigth_lenth - 1):
				self.weigth[i] += er * e[i] * self.epsilon
	
	def get_weigth(self):
		return self.weigth
# convert data to [x, y, label] and [ shuffle (just for testing) ]
data = []
for i in cluster1:
	data.append([i[0], i[1], 1])
for i in cluster2:
	data.append([i[0], i[1], -1])
random.shuffle(data)

# init 
e = 0.1
p = Perceptron(data, e)

# n training iteration 
n = 5
for i in range(0,n):
	#print(p.get_weigth())
	p.learn()

# check all data's expected label and predicted label
w = p.get_weigth()
for d in data:
	print("excepted : ", d[2])
	print("predicted : ", 1 if w[0]*d[0]+w[1]*d[1] >= 0 else -1)
	print()

#plt.show()
















