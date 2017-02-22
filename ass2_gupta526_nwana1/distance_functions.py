import csv
# File that calcualtes euclidean distance and cosine similarities for
# income and iris data sets. 
# File outputs the K most similar IDs for each transaction.

def euclidean_dist(p,q):
    e=0
    for m in range(0, len(p)-1):
        e = e + abs(p[m] - q[m])
    return (1 / len(p)) * e
def cosine_dist(p,q):
    num = 0
    denomp = 0
    denomq = 0
    for m in range(0, len(p)-1):
        num = num + (p[m] * q[m])
        denomp = denomp + p[m] * p[m]
        denomq = denomq + q[m] * q[m]
    return num / (denomp * denomq)

def create_header(k):
    header = ["Trans. ID"]
    for i in range(1, k + 1):
        header.append("ID")
        header.append("Symm")
        header.append("Class")
    return header

def iris_symmetry(calc,header):
    outE = open("iris_sym_euclidean.csv", 'w')
    wrE = csv.writer(outE, quoting=csv.QUOTE_ALL)
    wrE.writerow(header)
    for i in range(0, len(calc)):
        row = calc[i]
        id = row[0]
        e = row[1]
        rowE = [id]
        for i in range(0, len(e)):
            rowE.append(e[i])
        wrE.writerow(rowE)
    outE.close()


def income_symmetry(calc,header):
    outE=open("income_sym_euclidean.csv",'w')
    wrE = csv.writer(outE, quoting=csv.QUOTE_ALL)
    wrE.writerow(header)
    for i in range(0, len(calc)):
        row = calc[i]
        id = row[0]
        e = row[1]
        rowE = [id]
        for i in range(0, len(e)):
            rowE.append(e[i])
        wrE.writerow(rowE)
    outE.close()

def income_append(id,intop):
    top=[id]
    top.append(intop)
    return top

def iris_append(i,intop):
    top = [i]
    top.append(intop)
    return top


#input: iris or income
def output_symmetry():
    import csv
    dat=[]
    calc=[]
    #change if needed, where k is number of closest tuples
    k=5
    #choose e for euclidean distance, c for cosine distance
    symm="e"
    header=create_header(k)
    # change as needed for the dataset being run, i.e test or training
    #for iris
    with open("dataset/iris_test.csv") as file:
    #for income
    #with open("dataset/transformed_inc_test_file.csv") as file:
        with open("dataset/iris_test.csv") as file:
        #for income
        #with open("transformed_file.csv") as file:
            read=csv.reader(file)
            next(read)
            for row in read:
                p=row
                if not " ?" in p and not "?" in p:
                    for n in range(0, len(p)-1):
                        p[n]=float(p[n])
                    dat.append(p)
        file.close
        top5c = []
        top5e = []
        for s in range(0, 3 * k):
            top5c.append(-1)
            top5e.append(100000)
        for i in range(0, len(dat)):
            p=dat[i]
            for j in range(0, len(dat)):
                q=dat[j]
                if j!=i:
                    e=euclidean_dist(p,q)
                    e_rep = False
                    c=cosine_dist(p,q)
                    c_rep = False
                    seq=[]
                    for x in range(0,3*k):
                        if x%3==0:
                            seq.append(x)
                    for r in seq:
                        if e < top5e[r+1] and not e_rep:
                            e_rep=True
                            if(r<3*k-3):
                                top5e[r+3] = top5e[r]
                                top5e[r+4]=top5e[r+1]
                                top5e[r+5]=top5e[r+2]
                            top5e[r] = j
                            top5e[r+1] = e
                            top5e[r + 2] = q[-1]
                        if c> top5c[r+1] and not c_rep :
                            c_rep = True
                            if(r<3*k-3):
                                top5c[r + 3] = top5c[r]
                                top5c[r + 4] = top5c[r+1]
                                top5c[r+5]=top5c[r+2]
                            top5c[r] = j
                            top5c[r+1] = c
                            top5c[r + 2] = q[-1]
            #for income euclidean
            #top=income_append(p[0],top5e)
            # for income cosine
            # top=income_append(p[0],top5c)
            #for iris euclidean
            top=iris_append(i,top5e)
            #for iris cosine
            #top=iris_append(i,top5c)
            calc.append(top)
        iris_symmetry(calc,header)
        #income_symmetry(calc,header)
        # return output_income_symmetry(calc,header)
output_symmetry()