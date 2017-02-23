# File to get the K nearest neighbors and 
# classfy on the basis of majority vote
# input file: eculiden diatance iris or euclidean distance income

import csv, sys, os, string, operator
from collections import OrderedDict
# from read_input import transform_income



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
	for i in range(p,last_column_num,2):
		weight=1/neighbors[i]
		weight_class[weight]=neighbors[i+1]
	predicted_class = OrderedDict(sorted(weight_class.items()))
	class_ = predicted_class.popitem(False)
	return class_.values()

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
	header=("Transactuion ID", "Predicted Class", "Actual Class")
	iris_test_file = open("dataset/iris_sym_euclidean.csv")
	reader = csv.reader(iris_test_file)
	writer = csv.writer(iris_out_file)
	# k=5
	next(reader)
	writer.writerow(header)
	for row in reader:
		# print(row)
		predicted_class = getclass(row,3,k*3)
		actual_class = test_set_iris.get(row[0])
		result_row=(row[0],predicted_class,actual_class)
		writer.writerow(result_row)

	iris_out_file.close()
	iris_test_file.close()

def get_knn_income(k):
	test_set_income = getClassSetFromIncome()
	# print(type(test_set_income))
	income_out_file = open('output/knn_result_income.csv', 'w')
	header=("Transactuion ID", "Predicted Class", "Actual Class", "Posterior Probability")
	income_test_file = open("dataset/income_sym_euclidean.csv")
	reader = csv.reader(income_test_file)
	writer = csv.writer(income_out_file)
	next(reader)
	writer.writerow(header)
	for row in reader:
		id_ = row[0].split('.')
		predicted_class = getclass(row,0,k*3)
		actual_class = test_set_income.get(id_[0])
		probability = getProbability(predicted_class, row, k, 3)
		result_row=(row[0],predicted_class,actual_class, probability)
		writer.writerow(result_row)

	income_out_file.close()
	income_test_file.close()
	pass
def getProbability(predicted_class,neighbors,k,step):
	count = 0
	for i in range(step,len(neighbors),step)
		if neighbors[i]==predicted_class:
			count+=1
	probability = count/k
	return probability

def main():
	k=5
	get_knn_iris(k)
	get_knn_income(k)
	
main()
