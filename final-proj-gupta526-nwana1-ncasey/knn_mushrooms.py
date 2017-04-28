# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 10:21:45 2017

@author: Nicole
"""
# import packages
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# open the file
filepath = "E:/School/Data Mining Final Project/mushrooms.csv"
data = pd.read_csv(filepath)

# map variable letters to numbers
data['class'] = data['class'].map({'p': 0, 'e': 1})
data['cap-shape']=data['cap-shape'].map({'x':0,'b':1,'s':2,'f':3,'k':4,'c':5})
data['cap-surface']=data['cap-surface'].map({'s':0,'y':1,'f':2,'g':3})
data['cap-color']=data['cap-color'].map({'n':0,'y':1,'w':2,'g':3,'e':4,'p':5,'b':6,'u':7,'c':8,'r':9})
data['bruises']=data['bruises'].map({'f':0,'t':1})
data['odor']=data['odor'].map({'p':0,'a':1,'l':2,'n':3,'f':4,'c':5,'y':6,'s':7,'m':8})
data['gill-attachment']=data['gill-attachment'].map({'f':0,'a':1})
data['gill-spacing']=data['gill-spacing'].map({'c':0,'w':1})
data['gill-size']=data['gill-size'].map({'n':0,'b':1})
data['gill-color']=data['gill-color'].map({'k':0,'n':1,'g':2,'p':3,'w':4,'h':5,'u':6,'e':7,'b':8,'r':9,'y':10,'o':11})
data['stalk-surface-below-ring']=data['stalk-surface-below-ring'].map({'s':0,'f':1,'y':2,'k':3})
data['stalk-color-above-ring']=data['stalk-color-above-ring'].map({'w':0,'g':1,'p':2,'n':3,'b':4,'e':5,'o':6,'c':7,'y':8})
data['stalk-color-below-ring']=data['stalk-color-below-ring'].map({'w':0,'p':1,'g':2,'b':3,'n':4,'e':5,'y':6,'o':7,'c':8})
data['veil-type']=data['veil-type'].map({'p':0})
data['veil-color']=data['veil-color'].map({'w':0,'n':1,'o':2,'y':3})
data['ring-number']=data['ring-number'].map({'o':0,'t':1,'n':2})
data['ring-type']=data['ring-type'].map({'w':0,'g':1,'p':2,'n':3,'b':4,'e':5,'o':6,'c':7,'y':8})
data['spore-print-color']=data['spore-print-color'].map({'k':0,'n':1,'u':2,'h':3,'w':4,'r':5,'o':6,'y':7,'b':8})
data['population']=data['population'].map({'s':0,'n':1,'a':2,'v':3,'y':4,'c':5})
data['habitat']=data['habitat'].map({'u':0,'g':1,'m':2,'d':3,'p':4,'w':5,'l':6})
data['stalk-root']=data['stalk-root'].map({'e':0,'c':1,'b':2,'r':3,'?':4})
data['stalk-shape']=data['stalk-shape'].map({'e':0,'t':1})
data['stalk-surface-above-ring']=data['stalk-surface-above-ring'].map({'s':0,'f':1,'y':2,'k':3})

# split into train, test, and validation sets
train, test = train_test_split(data, test_size=0.3, random_state=0)

# split into data and class vectors
train_class = train['class']
test_class = test['class']
train_data = train.drop('class', 1)
test_data = test.drop('class', 1)

# create and fit a nearest-neighbor classifier
knn = KNeighborsClassifier()
# THIS IS WEHRE IT STOPS WORKING BECAUSE IT'S 'TOO LARGE'
knn.fit(train_data, train_class)
predictions = list(knn.predict(test_data))
score = knn.score(test_data, test_class)

# produce output dataframe
output = pd.DataFrame(test_class)
output['Predicted Class'] = pd.Series(predictions, index=output.index)
output = output.rename(columns={'class': 'Actual Class'})