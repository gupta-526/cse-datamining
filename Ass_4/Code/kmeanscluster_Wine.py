#k=("Enter number of clusters")
k=3
#list of [centroid number,simm]
#pick k centroids

def pick_centroids(k,dat):
    centroids=[]
    for i in len(dat):

    return centroids

def simmilarity(point,centroid):
    sim=100000
    return sim

def assign_cluster(point,centroids):
    cluster=-1
    #depending on which algorithm we use
    best_sim=100000
    centroid_sims=[]
    for centroid in centroids:
        centroid_sims.append([centroid,simmilarity(point,centroid)])
    for i in range(0,len(centroid_sims)):
        if centroid_sims[i[1]]<best_sim:
            best_sim=centroid_sims[i[1]]
            cluster=centroid_sims[i[0]]
    return cluster

def compute_centroid(cluster):
    centroid=-1
    return centroid
def output_file(clusters):




    return

def main():


