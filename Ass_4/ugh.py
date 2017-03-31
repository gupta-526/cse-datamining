import csv
import pandas as pd
from sklearn.cluster import KMeans


def analysis(name,k):
    data=pd.read_csv("Data/{0}".format(name))
    if name!="wine_quality-red.csv":
        data=data.drop("cluster",axis=1)
    else:
        data=data.drop("class",axis=1)
    km = KMeans(n_clusters=k, random_state=333)
    km.fit(data,y=None)
    labels=km.predict(data)
    labels=pd.DataFrame(labels)
    labels.to_csv("OffShelf/{0}".format(name))


def main():
    k=[2,4,2]
    j=0
    datas=["TwoDimEasy.csv","TwoDimHard.csv","wine_quality-red.csv"]
    for i in datas:
        analysis(i,k[j])
        j+=1

main()
