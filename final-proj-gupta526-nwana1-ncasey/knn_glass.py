# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 16:20:45 2017

@author: Nicole
"""
# import packages
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# open the file
filepath = "E:/School/Data Mining Final Project/glass.csv"
data = pd.read_csv(filepath)

# split into train, test, and validation sets
train, test = train_test_split(data, test_size=0.3, random_state=0)

# split into data and class vectors
train_class = train['Type']
test_class = test['Type']
train_data = train.drop('Type', 1)
test_data = test.drop('Type', 1)

# create and fit a nearest-neighbor classifier
knn = KNeighborsClassifier()
knn.fit(train_data, train_class)
predictions = list(knn.predict(test_data))
score = knn.score(test_data, test_class)

# produce output dataframe
output = pd.DataFrame(test_class)
output['Predicted Class'] = pd.Series(predictions, index=output.index)
output = output.rename(columns={'Type': 'Actual Class'})