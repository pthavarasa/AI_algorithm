from perceptron import Perceptron
from csv import reader

DEBUG = False

# csv file handling and data structure convert
with open('diabetes.csv') as f:
	next(f)
	reader = reader(f)
	data = []
	for line in reader:
		data.append([float(x) for x in line])

# init 
e = 0.1
p = Perceptron(data, e)

# n training iteration 
n = 100
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
