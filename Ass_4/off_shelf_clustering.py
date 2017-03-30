from sklearn.cluster import KMeans
import pandas as pd

def wine_cluster():
    wine=pd.read_csv("Data/wine_quality-redk=2,run2.csv")
    cluster=KMeans(n_clusters=3,random_state=11).fit(wine)
    cluster.labels_

def two_dim_cluster():
    easy = pd.read_csv("Data/TowDimEasy.csv")
    hard = pd.read_csv("Data/TowDimHard.csv")


def main():
    wine_cluster()
    two_dim_cluster()

main()