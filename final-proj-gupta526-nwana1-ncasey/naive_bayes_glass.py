from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import csv, pandas as pd
name="mushrooms.csv"
data = pd.read_csv("Dataset/{0}".format(name))
train, test = train_test_split(data, test_size=0.3, random_state=42)
train, verification=train_test_split(train, test_size=0.3, random_state=42)




data.to_csv("OffShelf/{0}".format(name))



def main():
    k=[2,7,2]
    j=0
    files=["breast_cancer.csv","mushrooms.csv","glass.csv"]
    for i in datas:
        analysis(i,k[j])
        j+=1

main()