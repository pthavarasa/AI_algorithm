import numpy as np
import matplotlib.pyplot as plt
from random import randint
from k_means import KMEANS

class KMEANS_Visualize(KMEANS):
  def __init__(self, k, data):
    KMEANS.__init__(self, k, data)
    # random color without red color (attributed to centers)
    self.color = ["#96%04x" % randint(0, 0xFFFF) for _ in range(self.k)]
  
  def show_cluster(self):
    for i in range(len(self.clusters)):
      plt.scatter([point[0] for point in self.clusters[i]], [point[1] for point in self.clusters[i]], color=self.color[i])

  def show_centers(self):
    for c in self.centers:
      plt.scatter(c[0], c[1], color="red")

  def learn(self):
    while True:
      self.assign_cluster()
      inertie = self.inertie_intra_classe()
      self.show_cluster()
      self.show_centers()
      plt.show()
      self.centroid()
      if not inertie > self.inertie_intra_classe(): break


centre1=np.array([3,3])
centre2=np.array([-3,-3])
centre3=np.array([3,-3])
sigma1=np.array([[1.5,0],[0,1.5]])
sigma2=np.array([[1.5,0],[0,1.5]])
sigma3=np.array([[1.5,0],[0,1.5]])
taille1=200
taille2=200
taille3=200
cluster1=np.random.multivariate_normal(centre1,sigma1,taille1)
cluster2=np.random.multivariate_normal(centre2,sigma2,taille2)
cluster3=np.random.multivariate_normal(centre3,sigma3,taille3)

KM = KMEANS_Visualize(3, [*cluster1, *cluster2, *cluster3])
KM.learn()
print(KM.centers)
