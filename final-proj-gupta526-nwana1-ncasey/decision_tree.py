# Author: Niharika
# import packages
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score

# split into train and test sets
def get_training_set(data,target):
	train_data, test_data, train_target, test_target = train_test_split(data, target , test_size=0.25, random_state=1)

	return(train_data, test_data, train_target, test_target)

def get_targets_cancer(data):
    # print "Target shape", data.shape
    df_mod = data.values[:, 3:33]
    targets = data.values[:, 2:3]
    # print "Target shape", targets
    return (df_mod, targets)

def get_targets_mushroom(data):

    df_mod = data.values[:, 2:24]
    targets = data.values[:, 1:2]
    # print "Target shape", targets

    return (df_mod, targets)

def get_targets_glass(data):

    print "Target shape", data.shape
    df_mod = data.values[:, 0:9]
    targets = data.values[:, 9:10]
    # print "Target shape", targets

    return (df_mod, targets)

# def get_targets_crime(data):

#     lst_col = data.shape[1]-1
#     print "Target shape", data.shape
#     df_mod = data.values[:, 2:19]
#     targets = data.values[:, 12:13]
#     # print "Target shape", targets

    # return (df_mod, targets)


def main():
	filepath_cancer = "./Dataset/breast_cancer_binary.csv"
	data_cancer = pd.read_csv(filepath_cancer)
	
	filepath_mushroom = "./Dataset/mushrooms_binary.csv"
	data_mushroom = pd.read_csv(filepath_mushroom)

	filepath_glass = "./Dataset/glass.csv"
	data_glass = pd.read_csv(filepath_glass)
	
	# filepath_crime = "./Dataset/Chicago_Crimes.csv"
	# data_crime = pd.read_csv(filepath_crime)

	data_mod_c, target_c = get_targets_cancer(data_cancer)
	data_mod_m, target_m = get_targets_mushroom(data_mushroom)
	data_mod_g, target_g = get_targets_glass(data_glass)
	print data_mod_g.shape
	print target_g.shape
	# data_mod_cc, target_cc = get_targets_crime(data_crime)
	
	#for cancer
	train_data, test_data, train_target, test_target = get_training_set(data_mod_c, target_c)
		# Decision Tree model with Gini Index accuracyPython
	decision_clf = DecisionTreeClassifier(criterion="entropy", splitter = "best", 
		random_state=100)
	decision_clf_cancer = decision_clf.fit(train_data, train_target)
	cancer_pred = decision_clf_cancer.predict(test_data)
	export_graphviz(decision_clf_cancer,out_file="cancer.dot")
	print "Cancer precision score", precision_score(test_target, cancer_pred)*100
	print "Cancer Accuracy is ", accuracy_score(test_target,cancer_pred)*100
	print "Cancer Confusion Matrix: \n", confusion_matrix(test_target, cancer_pred)
	

	#for crime
	# train_data_cc, test_data_cc, train_target_cc, test_target_cc = get_training_set(data_mod_cc, target_cc)
	# decision_clf_crime = DecisionTreeClassifier(criterion="entropy", splitter = "random", 
	# 	random_state=100)
	# decision_clf_crime = decision_clf_crime.fit(train_data_cc, train_target_cc)
	# crime_pred = decision_clf_crime.predict(test_data_cc)
	# print "Crime Accuracy is ", accuracy_score(test_target_cc,crime_pred)*100

	#for mushroom
	decision_clf_m = DecisionTreeClassifier(criterion="entropy", splitter = "best", 
		random_state=100)
	train_data_m, test_data_m, train_target_m, test_target_m = get_training_set(data_mod_m, target_m)
	decision_clf_mushroom = decision_clf_m.fit(train_data_m, train_target_m)
	mushroom_pred = decision_clf_mushroom.predict(test_data_m)
	export_graphviz(decision_clf_mushroom,out_file="mushroom.dot")
	print "Mushroom Precision Score: ", precision_score(test_target_m, mushroom_pred)*100
	print "Mushroom Accuracy is ", accuracy_score(test_target_m,mushroom_pred)*100
	print "Mushroom Confusion Matrix: \n", confusion_matrix(test_target_m, mushroom_pred)

	#for glass
	decision_clf_g = DecisionTreeClassifier(criterion="entropy", splitter = "best", 
		random_state=100)
	train_data_g, test_data_g, train_target_g, test_target_g = get_training_set(data_mod_g, target_g)
	decision_clf_glass = decision_clf_g.fit(train_data_g, train_target_g)
	glass_pred = decision_clf_glass.predict(test_data_g)
	print glass_pred
	export_graphviz(decision_clf_glass,out_file="glass.dot")
	print "Glass Precision ", precision_score(test_target_g,glass_pred, average="micro")*100
	print "Glass Accuracy is ", accuracy_score(test_target_g,glass_pred)*100
	print "Glass Confusion Matrix: \n", confusion_matrix(test_target_g, glass_pred)
	# print test_data

main()


