import csv

def initial_centroids(k,dat):
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


def assign_cluster(data,centroids):
    clusters=[]
    best_sim=10000
    centroid_sims=[]
    for i in range(0,len(data)):
        cluster = -1
        point=data[i]
        for centroid in centroids:
            #centroid_sims.append([centroid,two_dim_similarity(point,centroids)])
            #centroid_sims.append([centroid,wine_similarity(point,centroids)])
        for i in range(0,len(centroid_sims)):
            if centroid_sims[i[1]]<best_sim:
                best_sim=centroid_sims[i[1]]
                cluster=centroid_sims[i[0]]
        clusters.append([[point[0]],[cluster]])
    return clusters

def output_file(clusters,name):
    out= open("Output/{0}.csv".format(name),"w")
    wr=csv.writer(out,quoting=csv.QUOTE_ALL)
    wr.writerow(["ID"],["Cluster"])
    for row in range(0,len(clusters)):
        id=row[0]
        cluster=row[1]
        wr.writerow([id,cluster])
    out.close()

def input_file(name):
    data=[]
    infile =open("Dataset/{0}".format(name))
    read=csv.reader(infile)
    next(read)
    for row in read:
        for n in range(0,len(row)):
            row[n]=float(row[n])
        data.append(row)
    infile.close()
    return data

def main():
    #ask user for value of k
    k=3
    datas=["TwoDimEasy.csv","TwoDimHard.csv","wine_quality-red.csv"]
    for i in datas:
        data=input_file(datas[i])
        centroids=initial_centroids(k,data)
        clusters=assign_cluster(data,centroids)
        output_file(clusters,datas[i])
        
main()