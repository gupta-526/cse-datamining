from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import csv, pandas as pd, numpy as np


def predict(name):
    data = pd.read_csv("Dataset/{0}.csv".format(name))
    train, test = train_test_split(data, test_size=0.3, random_state=42)
    train, verification=train_test_split(train, test_size=0.3, random_state=42)
    gnb = GaussianNB()
    train_class = train['class']
    test_class = test['class']
    verification_class = verification['class']
    del train['class']
    print(gnb.fit(train,train_class))
    print(gnb.predict(verification))
    print(gnb.predict_proba(verification))
    pred=pd.DataFrame
    pred['Predicted Class']=gnb.predict(verification)
    pred['Actual Class']=verification_class
    pred['Probability']=gnb.predict_proba(verification)
    pred.to_csv("OffShelf/{0}".format(name))


def main():
    files=["breast_cancer","mushrooms","glass"]
    for i in files:
        predict(i)

main()