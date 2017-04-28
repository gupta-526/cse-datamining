import csv, pandas as pd, numpy as np
def mushroom_classes():
    name="mushroom"
    mush = pd.read_csv("Dataset/{0}.csv".format(name))
    mush['class'] = mush['class'].map({'p': 0, 'e': 1})
    mush.to_csv("Dataset/{0}_binary".format(name))

def cancer_classes():
    name="breast_cancer"
    cancer=pd.read_csv("Dataset/{0}.csv".format(name))
    cancer['class']=cancer['class'].map({'M':1, 'B':0})
    cancer.to_csv("Dataset/{0}_binary".format(name))
