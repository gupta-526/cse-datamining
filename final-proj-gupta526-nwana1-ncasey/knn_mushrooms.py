# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 16:19:48 2017

@author: Nicole
"""
# import packages
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# open the file
filepath = "E:/School/Data Mining Final Project/cancer.csv"
data = pd.read_csv(filepath)

# split into train and test sets
train, test = train_test_split(data, test_size=0.3, random_state=0)

# drop NaN column
train = train.ix[:, 0:32]
test = test.ix[:, 0:32]

# split into data and class vectors
train_class = train['diagnosis']
test_class = test['diagnosis']
train_data = train.drop('diagnosis', 1)
test_data = test.drop('diagnosis', 1)

# create and fit a nearest-neighbor classifier
knn = KNeighborsClassifier()
knn.fit(train_data, train_class)
predictions = list(knn.predict(test_data))
score = knn.score(test_data, test_class)

# produce output dataframe
output = pd.DataFrame(test_class)
output['Predicted Class'] = pd.Series(predictions, index=output.index)
output = output.rename(columns={'diagnosis': 'Actual Class'})
