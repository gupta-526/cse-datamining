Assignment: Lab 2
Name: Niharika Gupta, Marielle Nwana
Date: February 22, 2017
Language used: Python (3.X)

Step1: 
Edit and transform input datasets to create training sets:

	python read_input.py

	-this will generate required transformed files in the dataset folder

Step 2: 
Get euclidean distance of all:
	
	* for iris test and training dataset:

	python distance_functions.py
	
	- this will generate iris_sym_euclidean.csv file 

	* for income test and training dataset:
		- comment out the neccesary parts and and uncomment the necessary parts

		run distance_functions again. 

		python distance_functions.py 

	* for income test (original test file):
		- will give transformed_inc_test_full.csv in the dataset folder

		python distance_test_full.py


Step 3:
Get classification of k-nearest neighbors:
	- this will create knn_result_iris.csv and knn_result_income.csv in the output folder
	
	python knn_implementation.py
	
	


Work division
	-distance.py(M)
	-read_input(N)
	-knn_implementation(N)
	-performance_eval(M)
	(true positive rates, true negative, false positive rates, false negative , ROC plot(slide 96+77) precision, recall and f-measure (slide 83))
	-shelf_implementation