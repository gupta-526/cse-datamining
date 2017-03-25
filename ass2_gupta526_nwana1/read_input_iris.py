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

	

	out_iris_test.close()
	# out_iris_training.close()
	input_test.close()
	# input_train.close()

