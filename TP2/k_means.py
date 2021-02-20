from random import randint
from random import choice
import numpy as np
import matplotlib.pyplot as plt


class KMEANS:
  def __init__(self, k, data):
    self.k = k
    self.data = data
    self.clusters = []
    self.centers = []
  
  def init_clusters(self):
    for _ in range(self.k):
      self.clusters.append([])
  
  def init_centers(self):
    while len(self.centers) != self.k:
      random_data = choice(self.data)
      if random_data not in self.centers:
        self.centers.append(random_data)
  
  def distance(self, p1, p2):
    sum = 0
    for i in range(len(p1)):
      sum += abs(p1[i] - p2[i])
    return sum

  def assign_cluster(self):
    self.clusters = []
    self.init_clusters()
    for d in self.data:
      dist = -1
      cluster = 0
      for i in range(len(self.centers)):
        if dist == -1:
          dist = self.distance(self.centers[i], d)
        elif dist > self.distance(self.centers[i], d):
          cluster = i
      self.clusters[cluster].append(d)

  def centroid(self):
    for c in range(len(self.clusters)):
      length = len(self.clusters[c])
      sum = []
      for i in self.clusters[c][0]:
        sum.append(0)
      for d in self.clusters[c]:
        for e in range(len(d)):
          sum[e] += d[e]
      for i in range(len(sum)):
        sum[i] = sum[i] * (1/length)
      self.centers[c] = sum
  
  def show_cluster(self):
    color = ['pink', 'blue']
    for i in range(len(self.clusters)):
      plt.scatter([point[0] for point in self.clusters[i]], [point[1] for point in self.clusters[i]], color=color[i])
  
  def show_centers(self):
    for c in self.centers:
      plt.scatter(c[0], c[1], color="red")

  def inertie_intra_classe(self):
    sum = 0
    for c in range(self.k):
      for i in range(len(self.clusters[c])):
        sum += pow(self.distance(self.clusters[c][i], self.centers[c]), 2)
    return sum
  
  def run(self):
    #plt.scatter([point[0] for point in self.data], [point[1] for point in self.data], color="pink")
    #plt.show()
    self.init_clusters()
    self.init_centers()
    #print(self.clusters)
    #print(self.centers)
    condition = True
    while condition:
      #print(self.clusters)
      #print(self.clusters)
      #print(self.centers)
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

