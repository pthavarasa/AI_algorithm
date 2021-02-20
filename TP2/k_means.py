from random import randint
from random import choice
from random import sample
import numpy as np
import matplotlib.pyplot as plt


class KMEANS:
  def __init__(self, k, data):
    self.k = k
    self.data = data
    self.clusters = [[] for _ in range(self.k)]
    self.centers = sample(self.data, self.k)
    self.color = ["#96%04x" % randint(0, 0xFFFF) for _ in range(self.k)]
  
  def distance(self, p1, p2):
    return sum(abs(p1[i] - p2[i]) for i in range(len(p1)))

  def assign_cluster(self):
    self.clusters = [[] for _ in range(self.k)]
    for d in self.data:
      self.clusters[min((val, id) for (id, val) in enumerate(self.distance(self.centers[k], d) for k in range(self.k)))[1]].append(d)

  def centroid(self):
    self.centers = [[sum(d) * (1/len(c)) for d in zip(*c)] for c in self.clusters]
  
  def show_cluster(self):
    for i in range(len(self.clusters)):
      plt.scatter([point[0] for point in self.clusters[i]], [point[1] for point in self.clusters[i]], color=self.color[i])
  
  def show_centers(self):
    for c in self.centers:
      plt.scatter(c[0], c[1], color="red")

  def inertie_intra_classe(self):
    return sum(pow(self.distance(i, self.centers[c]), 2) for c in range(self.k) for i in self.clusters[c])
  
  def run(self):
    condition = True
    while condition:
      self.assign_cluster()
      inertie = self.inertie_intra_classe()
      self.show_cluster()
      self.show_centers()
      plt.show()
      self.centroid()
      condition = inertie > self.inertie_intra_classe()




centre1=np.array([3,3])
centre2=np.array([-3,-3])
sigma1=np.array([[1.5,0],[0,1.5]])
sigma2=np.array([[1.5,0],[0,1.5]])
taille1=200
taille2=200
cluster1=np.random.multivariate_normal(centre1,sigma1,taille1)
cluster2=np.random.multivariate_normal(centre2,sigma2,taille2)

data = []
for i in cluster1:
	data.append([i[0], i[1]])
for i in cluster2:
	data.append([i[0], i[1]])

KM = KMEANS(2, data)
KM.run()

#plt.scatter([point[0] for point in cluster1], [point[1] for point in cluster1], color="pink")
#plt.scatter([point[0] for point in cluster2], [point[1] for point in cluster2], color="blue")
#plt.scatter(centre1[0], centre1[1], color="red")
#plt.scatter(centre2[0], centre2[1], color="red")

#plt.show()

