import csv, pandas as pd, numpy as np
def mushroom_classes():
    mush = pd.read_csv("Dataset/mushroom.csv")
    mush['class'] = mush['class'].map({'female': 1, 'male': 0})
