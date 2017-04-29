from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import pandas as pd


def predict(name):
    data = pd.read_csv("Dataset/{0}.csv".format(name))
    train, test= train_test_split(data, test_size=0.3, random_state=0)
    gnb = GaussianNB()
    train_class = train['class']
    test_class = test['class']
    del test['class']
    del train['class']
    gnb.fit(train,train_class)
    pred=pd.DataFrame
    pred['Predicted Class']=gnb.predict(test)
    pred['Actual Class']=test_class
    pred['Probability']=gnb.predict_proba(test)
    pred.to_csv("Output/{0}".format(name))


def main():
    files=["breast_cancer_binary","mushrooms_binary","glass"]
    for i in files:
        predict(i)

main()

