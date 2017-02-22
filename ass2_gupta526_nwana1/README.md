Assignment: Lab 2
Name: Niharika Gupta, Marielle Nwana
Date: February 22, 2017
Language used: Python (3.X)

Edit and transform input datasets to create training sets:

	python read_input.py

	-this will generate required transformed files in the dataset folder

Get euclidean distance of all:
	
	* for iris dataset:

	python distance_functions.py
	
	- this will generate iris_sym_euclidean.csv file 

	* for income dataset:
		- comment out the neccesary parts and and uncomment the necessary parts

		run distance_functions again. 

		python distance_functions.py 

Get classification of k-nearest neighbors:
	
	python knn_implementation.py
	
	- this will create knn_result_iris.csv and knn_result_income.csv in the output folder 



//work division
	-distance.py(M)
	-read_input(N)
	-knn_implementation(N)
	-performance_eval(M)
	(true positive rates, true negative, false positive rates, false negative , ROC plot(slide 96+77) precision, recall and f-measure (slide 83))
	-shelf_implementation