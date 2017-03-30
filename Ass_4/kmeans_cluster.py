import csv, random


MAX_ITERATIONS=1000


#complete
def initialize_centroids(data, k):
    length = len(data)
    centroids=[]
    # test = random.choice(data)
    for i in range(0, int(k)):
        centroids.append(random.randint(1,length-1))
    return centroids


#complete
def two_dim_calculate_centroid(data,old_centroids,old_clusters):
    new_centroids=old_centroids.copy()
    for j in range(0,len(old_centroids)):
        avg_one = 0
        avg_two = 0
        count = 1
        for i in range(0, len(old_clusters)):
            if old_centroids[j] == old_clusters[i]:
                count = count+1
                avg_one+=data[i][1]
                avg_two+=data[i][2]
        avg_one=avg_one/count
        avg_two=avg_two/count
        avg=[-1,avg_one,avg_two,-1]
        best_sim=1000
        for i in range(0,len(data)):
            if old_centroids[j] == old_clusters[i]:
                sim=two_dim_similarity(data[i],avg)
                if sim<best_sim:
                    new_centroids[j] = i
                    best_sim=sim
    return new_centroids


#incomplete
def wine_calculate_centroid(data,old_centroids,old_clusters):
    new_centroids=old_centroids.copy()
    for j in range(0,len(old_centroids)):
        count = 1
        avg=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
        for i in range(0, len(old_clusters)):
            if old_centroids[j] == old_clusters[i]:
                count+=1
                for m in range(1,len(data[i])-1):
                    avg[m]+=data[i][m]
        for x in range(1,len(avg)-1):
                avg[x]=avg[x]/count
        best_sim=1000
        for i in range(0,len(data)):
            if old_centroids[j] == old_clusters[i]:
                sim=wine_similarity(data[i],avg)
                if sim<best_sim:
                    best_sim=sim
                    new_centroids[j]=i
    return new_centroids


#complete
def two_dim_similarity(point,centroid):
    e = 0
    q=centroid
    for m in range(1,3 ):
        e+=abs(point[m] - q[m])
    return (1 /(len(point)-1)) * e


#complete
def wine_similarity(point,centroid):
    e = 0
    q=centroid
    for m in range(1,len(point)-1):
        e = e + abs(point[m] - q[m])
    if point[-1]!=q[-1]:
        e+=1
    return (1 /(len(point)-1)) * e


#complete
def wine_assign_cluster(data,centroids):
    clusters=[]
    for i in range(0,len(data)):
        best_sim = 100000
        cluster = -1
        point=data[i]
        for centroid in centroids:
            sim=wine_similarity(point,data[centroid])
            if sim<best_sim:
                best_sim=sim
                cluster=centroid
        clusters.append(cluster)
    return clusters


#complete
def two_dim_assign_cluster(data,centroids):
    clusters=[]
    for i in range(0,len(data)):
        best_sim = 10000
        cluster = -1
        point=data[i]
        for centroid in centroids:
            sim=two_dim_similarity(point,data[centroid])
            if sim<best_sim:
                best_sim=sim
                cluster=centroid
        clusters.append(cluster)
    return clusters


#complete
def does_converge(old,new,iteration):
        if iteration> MAX_ITERATIONS:
            return True
        return old == new


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


#complete
def main():
    #ask user for value of k
    #k=get_user_input()
    k=get_user_input()
    x=0
    datas=["TwoDimEasy.csv","TwoDimHard.csv"]
    for i in datas:
        # k=ks[x]
        # if(int(k)<5):
        converges=False
        data=input_file(i)
        iteration = 0
        centroids = initialize_centroids(data, k)
        old_clusters=two_dim_assign_cluster(data,centroids)
        new_clusters=old_clusters
        while not converges:
            iteration+=1
            centroids=two_dim_calculate_centroid(data,centroids,old_clusters)
            old_clusters=new_clusters
            new_clusters=two_dim_assign_cluster(data,centroids)
            converges=does_converge(old_clusters,new_clusters,iteration)
        for m in range(0,len(centroids)):
            for j in range(0,len(data)):
                if new_clusters[j]==centroids[m]:
                    new_clusters[j]=m+1
        output_file(new_clusters, i)
        # x+=1
        
    name="wine_quality-red.csv"
    # k=ks[-1]
    # if(int(k)<=4):
    converges = False
    data = input_file(name)
    iteration = 0
    centroids = initialize_centroids(data, k)
    old_clusters = wine_assign_cluster(data, centroids)
    new_clusters = old_clusters.copy()
    while not converges:
        iteration += 1
        centroids = wine_calculate_centroid(data,centroids,old_clusters)
        old_clusters=new_clusters
        new_clusters = wine_assign_cluster(data, centroids)
        converges = does_converge(old_clusters, new_clusters, iteration)
    for m in range(0, len(centroids)):
        for j in range(0, len(data)):
            if new_clusters[j] == centroids[m]:
                new_clusters[j] = m + 1
    output_file(new_clusters, name)
    # y+=1

main()
