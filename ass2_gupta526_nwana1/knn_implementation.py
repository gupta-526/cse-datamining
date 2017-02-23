# File to get the K nearest neighbors and 
# classfy on the basis of majority vote
# input file: eculiden diatance iris or euclidean distance income

import csv, sys, os, string, operator
from collections import OrderedDict
# from read_input import transform_income


header=("Transaction ID", "Weighted Class", "Predicted Class", "Actual Class", 
	"Posterior Probability", "Posterior Probability with Weight")
def getclass(neighbors,p,last_column_num):
	classVotes={}
	last_column_num= last_column_num+3
	# print(last_column_num)


	for i in range(p,last_column_num,3):
		# get class and then add to class votes
		# print(i)
		# print(neighbors[i])
		class_ = neighbors[i]
		if class_ in classVotes:
			classVotes[class_] += 1
		else:
			classVotes[class_] = 1
		# i = i+3
		# print(i)
	predicted_class = sorted(classVotes.items(), key=operator.itemgetter(1), 
						reverse=True)
	return (predicted_class[0][0])

def getClassFromWeight(neighbors,p,last_column_num):
	weight_class={}
	last_column_num+=2
	# print(neighbors)
	for i in range(p,last_column_num,3):
		# symm= neighbors[i].split('.')
		# print(symm)
		weight = 0
		if not (float(neighbors[i]) == 0.0):
			weight=1.0/float(neighbors[i])
		weight_class[weight]=neighbors[i+1]
	predicted_class = OrderedDict(sorted(weight_class.items()))
	class_ = predicted_class.popitem(False)
	# print(class_)
	return class_[1]

def getClassSetFromIris():
	iris_test_file = open("dataset/transformed_iris_test_file.csv")
	reader = csv.reader(iris_test_file)
	# test_set={id:class}
	test_set = {}
	next(reader)
	for row in reader:
		# key=row[5]
		# value=row[4]
		test_set[row[5]]=row[4]
	iris_test_file.close()
	# print(test_set)
	return test_set

def getClassSetFromIncome():
	income_test_file = open("dataset/transformed_inc_Test_full.csv")
	reader = csv.reader(income_test_file)
	test_set = {}
	next(reader)
	for row in reader:
		# print(row[0])
		# print(row[15])
		test_set[row[0]]= row[13]
	income_test_file.close()
	# print(test_set)
	return test_set

def get_knn_iris(k):
	test_set_iris = getClassSetFromIris()
	iris_out_file = open('output/knn_result_iris.csv', 'w')
	iris_test_file = open("dataset/iris_sym_euclidean.csv")
	reader = csv.reader(iris_test_file)
	writer = csv.writer(iris_out_file)
	filename = "iris_full_euclidean.csv"
	# k=5
	next(reader)
	writer.writerow(header)
	for row in reader:
		# print(row)
		# weight_predicted_class=getClassFromWeight(row,2,k*2)
		predicted_class = getclass(row,3,k*3)
		actual_class = test_set_iris.get(row[0])
		probability = getProbability(row[0], predicted_class, k, filename)
		# probability_wght = getProbability(row[0], weight_predicted_class, k, filename)
		result_row=(row[0],predicted_class,actual_class, probability)
		# result_row=(row[0],weight_predicted_class,predicted_class,actual_class, probability, probability_wght)
		writer.writerow(result_row)

	iris_out_file.close()
	iris_test_file.close()

def get_knn_income(k):
	test_set_income = getClassSetFromIncome()
	# print(type(test_set_income))
	income_out_file = open('output/knn_result_income.csv', 'w')
	income_test_file = open("dataset/income_sym_euclidean.csv")
	reader = csv.reader(income_test_file)
	writer = csv.writer(income_out_file)
	filename = "income_sym_euclidean.csv"
	next(reader)
	writer.writerow(header)
	for row in reader:
		id_ = row[0].split('.')
		# weight_predicted_class=getClassFromWeight(row,2,k*2)
		predicted_class = getclass(row,0,k*3)
		actual_class = test_set_income.get(id_[0])
		probability = getProbability(id_[0],predicted_class, k, filename)
		# probability_wght = getProbability(id_[0], weight_predicted_class, k, filename)
		result_row=(row[0],predicted_class,actual_class, probability)
		# print(weight_predicted_class)
		writer.writerow(result_row)

	income_out_file.close()
	income_test_file.close()
	pass
def getProbability(id_, predicted_class,k,filename):
	count = 0
	probability = "nope"
	input_file = open(filename)
	reader = csv.reader(input_file)
	for row in reader:
		_id_=row[0].split('.')
		# print(_id_[0])
		# print(id_)
		if id_==_id_[0]:
			for i in range(1,len(row)):
				if row[i]==predicted_class:
					count+=1
			probability = count/k
	return probability

def main():
	k=5
	get_knn_iris(k)
	get_knn_income(k)
	
main()
