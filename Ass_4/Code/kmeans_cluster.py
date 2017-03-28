import csv
#k=("Enter number of clusters")
k=3
#list of [centroid number,simm]
#pick k centroids

def pick_centroids(k,dat):
    centroids=[]
    for i in len(dat):
        #do something
    return centroids

def two_dim_similarity(point,centroid):
    e = 0
    for m in range(1,3 ):
        e = e + abs(point[m] - centroid[m])
    return (1 /(len(point)-1)) * e

def wine_similarity(point,centroid):
    e = 0
    for m in range(1,13):
        e = e + abs(point[m] - centroid[m])
    if point[-1]!=centroid[-1]:
        e=e+1
    return (1 /(len(point)-1)) * e


def assign_cluster(point,centroids):
    cluster=-1
    best_sim=10000
    centroid_sims=[]
    for centroid in centroids:
        #centroid_sims.append([centroid,two_dim_similarity(point,centroid)])
        #centroid_sims.append([centroid,wine_similarity(point,centroid)])
    for i in range(0,len(centroid_sims)):
        if centroid_sims[i[1]]<best_sim:
            best_sim=centroid_sims[i[1]]
            cluster=centroid_sims[i[0]]
    return cluster

def compute_centroid(cluster):
    centroid=-1
    return centroid

def output_file(clusters):


#check if the cluster is right or not
def compare_clustering(p):


def main():


main()