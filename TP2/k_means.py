from random import randint
from random import choice
from random import sample


class KMEANS:
  """KMEANS class :)
  Attribute : 
  - k : Clusters lenght
  - data : Multidimensional data array
  Methods :
  - distance : Euclidean distance of 2 array
  - assign_cluster : Assign objects to their closest cluster center according to the Euclidean distance
  - centroid : Calculate the centroid or mean of all objects in each cluster
  - inertie_intra_classe : Total intra-cluster variance
  - learn : Repeat func assign_cluster and centroid until the same points are assigned to each cluster in consecutive rounds
  Note : Unoptimized code - https://code.up8.edu/pthavarasa/ai-tp/-/commit/a26271ce7ba173ccbc729ef7e10769cdada9d588
  """
  def __init__(self, k, data):
    self.k = k
    self.data = data
    self.clusters = [[] for _ in range(self.k)]
    self.centers = sample(self.data, self.k)
  
  def distance(self, p1, p2):
    return sum(abs(p1[i] - p2[i]) for i in range(len(p1)))

  def assign_cluster(self):
    self.clusters = [[] for _ in range(self.k)]
    for d in self.data:
      self.clusters[min((val, id) for (id, val) in enumerate(self.distance(self.centers[k], d) for k in range(self.k)))[1]].append(d)

  def centroid(self):
    self.centers = [[sum(d) * (1/len(c)) for d in zip(*c)] for c in self.clusters]

  def inertie_intra_classe(self):
    return sum(pow(self.distance(i, self.centers[c]), 2) for c in range(self.k) for i in self.clusters[c])
  
  def learn(self):
    while True:
      self.assign_cluster()
      inertie = self.inertie_intra_classe()
      self.centroid()
      if not inertie > self.inertie_intra_classe(): break
