from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import pandas as pd


def predict(name):
    data = pd.read_csv("Dataset/{0}.csv".format(name))
    train, test= train_test_split(data, test_size=0.33, random_state=0)
    gnb = GaussianNB()
    train_class = train['class']
    test_class = pd.DataFrame(test['class'])
    test_class.columns=['Actual Class']
    del test['class']
    del train['class']
    gnb.fit(train,train_class)
    test_df = pd.DataFrame()
    test_df['ID']=test.index
    test_df['Predicted Class']=gnb.predict(test)
    test_class['ID']=test.index
    test_df=pd.merge(test_df,test_class,how='left',left_on=test_df['ID'],right_on=test_class['ID'],copy=False)
    out=pd.DataFrame(gnb.predict_proba(test))
    out=pd.concat([test_df,out],axis=1)
    out.to_csv("Naive_Output/{0}.csv".format(name),index=False)


def main():
    files=["breast_cancer_binary","mushrooms_binary","glass"]
    for i in files:
        predict(i)

main()

