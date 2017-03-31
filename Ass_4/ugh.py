import csv
import pandas as pd
from sklearn.cluster import KMeans

#complete
def output_file(clusters,name):
    out= open("Output/{0}".format(name),"w")
    wr=csv.writer(out,quoting=csv.QUOTE_ALL)
    wr.writerow(["ID","Cluster"])
    for i in range(0,len(clusters)):
        id=i+1
        cluster=clusters[i]
        wr.writerow([id,cluster])
    out.close()


#complete
def input_file(name):
    data=[]
    infile =open("Data/{0}".format(name))
    read=csv.reader(infile)
    next(read)
    if name != "wine_quality-red.csv":
        for row in read:
            for n in range(0,len(row)):
                row[n]=float(row[n])
            data.append(row)
    else:
        for row in read:
            for n in range(0,len(row)-1):
                row[n]=float(row[n])
            data.append(row)
    infile.close()
    return data


def analysis(name,k):
    data=pd.read_csv("Data/{0}".format(name))
    if name!="wine_quality-red.csv":
        data=data.drop("cluster",axis=1)
    else:
        data=data.drop("class",axis=1)
    cluster = KMeans(n_clusters=k, random_state=11)
    cluster.fit(data)
    clusters=cluster.labels_
    clusters=pd.DataFrame(clusters)
    clusters.to_csv("OffShelf/{0}".format(name))

#complete
def main():
    k=[2,4,2]
    j=0
    datas=["TwoDimEasy.csv","TwoDimHard.csv","wine_quality-red.csv"]
    for i in datas:
        analysis(i,k[j])
        j+=1

main()
