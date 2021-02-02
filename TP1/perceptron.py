from random import randint

class Perceptron:
	def __init__(self, data, e):
		self.weigth_lenth = len(data[0])
		self.epsilon = e
		self.weigth = []
		self.weigth_init()
		self.data = data

	def weigth_init(self):
		for i in range(0, self.weigth_lenth):
			self.weigth.append(randint(0,1))
		return self.weigth

	def decision(self, x):
		s = self.weigth[self.weigth_lenth - 1]
		for i in range(0, self.weigth_lenth - 1):
			s += self.weigth[i] * x[i]
		return 1 if s >= 0 else 0

	def learn(self):
		for e in self.data:
			d = self.decision(e)
			er = e[self.weigth_lenth - 1] - d
			self.weigth[self.weigth_lenth - 1] += er * self.epsilon
			for i in range(0, self.weigth_lenth - 1):
				self.weigth[i] += er * e[i] * self.epsilon
	
	def get_weigth(self):
		return self.weigth

	def get_weigth_lenth(self):
		return self.weigth_lenth