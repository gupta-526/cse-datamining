# File to transform the income data set.
# File transforms the nominal attributes and assigns each 
# attribute an interger

import csv, sys, os, string
def transform_iris():
	header=["sepal_length","sepal_width","petal_length","petal_width","class","id"]
	input_test = open("dataset/Iris_Test.csv", 'r')
	out_iris_test = open('dataset/transformed_iris_test_file.csv', 'w')
	reader_test = (csv.reader(input_test))
	writer_test = csv.writer(out_iris_test)
	new_row = ()
	i = 0
	next(reader_test)
	writer_test.writerow(header)
	for row in reader_test:
		new_row=row.copy()
		new_row.append(i)
		# new_row.fromlist(row)
		i=i+1
		writer_test.writerow(new_row)
		new_row.clear()

	# input_train = open("dataset/iris_training.csv",'r')
	# out_iris_training = open('dataset/transformed_iris_training.csv', 'w')
	# reader_train = (csv.reader(input_train))
	# writer_train = (csv.writer(out_iris_training))

	# j = 0
	# next(reader_train)
	# writer_train.writerow(header)
	# for row in reader_train:
	# 	new_row=row.copy()
	# 	new_row.append(j)
	# 	# new_row.append(str(j))
	# 	# new_row.fromlist(row)
	# 	# print(new_row)
	# 	j=j+1
	# 	writer_train.writerow(new_row)
	# 	new_row.clear()


	out_iris_test.close()
	# out_iris_training.close()
	input_test.close()
	# input_train.close()

