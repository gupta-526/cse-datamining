import csv, random, os, sys


MAX_ITERATIONS=1000


#incomplete
def initialize_centroids(data, k):
    length = len(data)
    centroids=[]
    # test = random.choice(data)
    for i in range(0, k):
        centroids.append(random.randint(1,length-1))
    # print(test)
    return centroids


#incomplete
def reassign_centroids(data,k,centroids):

    return centroids


#incomplete
def is_outlier(point,centroid,data):
    1


#complete
def two_dim_similarity(point,centroid):
    e = 0
    for m in range(1,3 ):
        e+=abs(point[m] - centroid[m])
    return (1 /(len(point)-1)) * e


#complete
def wine_similarity(point,centroid):
    e = 0
    for m in range(1,13):
        e = e + abs(point[m] - centroid[m])
    if point[-1]!=centroid[-1]:
        e+=1
    return (1 /(len(point)-1)) * e


#complete
def wine_assign_cluster(data,centroids):
    clusters=[]
    best_sim=100000
    for i in range(0,len(data)):
        cluster = -1
        point=data[i]
        for centroid in centroids:
            sim=[centroid,wine_similarity(point,centroid)]
            if sim<best_sim:
                best_sim=sim
                cluster=centroid[0]
        clusters.append(cluster)
    return clusters


#complete
def two_dim_assign_cluster(data,centroids):
    clusters=[]
    best_sim=10000
    for i in range(0,len(data)):
        cluster = -1
        point=data[i]
        for centroid in centroids:
            sim=[centroid,two_dim_similarity(point,centroids)]
            if sim<best_sim:
                best_sim=sim
                cluster=centroid[0]
        clusters.append(cluster)
    return clusters


#complete
def does_converge(old,new,iter):
        if iter> MAX_ITERATIONS:
            return True
        return old==new


#complete
def output_file(clusters,name):
    out= open("Output/{0}".format(name),"w")
    wr=csv.writer(out,quoting=csv.QUOTE_ALL)
    wr.writerow(["ID","Cluster"])
    for row in clusters:
        id=row[0]
        cluster=row[1]
        wr.writerow(id,cluster)
    out.close()


#complete
def input_file(name):
    data=[]
    infile =open("Data/{0}".format(name))
    read=csv.reader(infile)
    next(read)
    if name!="wine_quality-red.csv":
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

#complete
def get_user_input():
    k_val = input("Please enter a value for k: ")
    return k_val


#incomplete
def main():
    #ask user for value of k
    k=get_user_input()
    datas=["TwoDimEasy.csv","TwoDimHard.csv"]
    for i in datas:
        converges=False
        data=input_file(i)
        itter = 0
        centroids = initialize_centroids(data, k)
        old_clusters=two_dim_assign_cluster(data,centroids)
        new_clusters=[]
        while not converges:
            itter+=1
            centroids=reassign_centroids(data,k,centroids)
            new_clusters=two_dim_assign_cluster(data,centroids)
            converges=does_converge(old_clusters,new_clusters)
            centroids=initialize_centroids(data,k)
            output_file(new_clusters,i)
    data="wine_quality-red.csv"
    converges = False
    data = input_file(i)
    itter = 0
    centroids = initialize_centroids(data, k)
    old_clusters = two_dim_assign_cluster(data, centroids)
    new_clusters = []
    while not converges:
        itter += 1
        centroids = reassign_centroids(data, k, centroids)
        new_clusters = wine_assign_cluster(data, centroids)
        converges = does_converge(old_clusters, new_clusters)
        centroids = initialize_centroids(data, k)
        output_file(new_clusters, i)

main()
