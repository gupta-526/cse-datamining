
def euclidean_dist(p,q):
    e=0
    for m in range(0, len(p)):
        e = e + abs(p[m] - q[m])
    return (1 / len(p)) * e
def cosine_dist(p,q):
    num = 0
    denomp = 0
    denomq = 0
    for m in range(0, len(p)):
        num = num + (p[m] * q[m])
        denomp = denomp + p[m] * p[m]
        denomq = denomq + q[m] * q[m]
    return num / (denomp * denomq)

def create_header(k):
    header = ["Trans. ID"]
    for i in range(1, k + 1):
        header.append("ID")
        header.append("Symm")
    return header

def output_iris_symmetry(calc):
    outE = open("iris_sym_euclidean.csv", 'w')
    outC = open("iris_sym_cosine.csv", "w")
    wrE = csv.writer(outE, quoting=csv.QUOTE_ALL)
    wrC = csv.writer(outC, quoting=csv.QUOTE_ALL)
    wrE.writerow(header)
    wrC.writerow(header)
    for i in range(0, len(calc)):
        row = calc[i]
        id = row[0]
        e = row[1]
        c = row[2]
        rowC = [id]
        rowE = [id]
        for i in range(0, len(e)):
            rowC.append(c[i])
            rowE.append(e[i])
        wrC.writerow(rowC)
        wrE.writerow(rowE)
    outE.close()
    outC.close()


def output_income_symmetry(calc):
    outE=open("income_sym_euclidean.csv",'w')
    outC=open("income_sym_cosine.csv","w")
    wrE = csv.writer(outE, quoting=csv.QUOTE_ALL)
    wrC = csv.writer(outC, quoting=csv.QUOTE_ALL)
    wrE.writerow(header)
    wrC.writerow(header)
    for i in range(0, len(calc)):
        row = calc[i]
        id = row[0]
        e = row[1]
        c = row[2]
        rowC = [id]
        rowE = [id]
        for i in range(0, len(e)):
            rowC.append(c[i])
            rowE.append(e[i])
        wrC.writerow(rowC)
        wrE.writerow(rowE)
    outE.close()
    outC.close()

def income_append(id,top5e,top5c):
    top=[id]
    top.append(top5e)
    top.append(top5c)
    return top

def iris_append(i,top5c,top5e):
    top = [i]
    top.append(top5e)
    top.append(top5c)
    return top


#input: iris or income
import csv
dat=[]
calc=[]
#change if needed, where k is number of closest tuples
k=5
header=create_header(k)
#for iris
with open("dataset/iris_test.csv") as file:
#for income
#with open("transformed_file.csv") as file:
    read=csv.reader(file)
    next(read)
    for row in read:
        p=row
        #next line used for iris only. comment out if for income
        p=p[0:4]
        if not " ?" in p and not "?" in p:
            for n in range(0, len(p)):
                p[n]=float(p[n])
            dat.append(p)
for i in range(0, len(dat)):
    p=dat[i]
    top5c=[]
    top5e=[]
    for s in range(0,2*k):
        top5c.append(-1)
        top5e.append(100000)
    for j in range(0, len(dat)):
        q=dat[j]
        if j!=i:
            e=euclidean_dist(p,q)
            c=cosine_dist(p,q)
            e_rep = False
            c_rep = False
            seq=[]
            for x in range(1,2*k):
                if x%2!=0:
                    seq.append(x)
            for r in seq:
                if e < top5e[r] and not e_rep:
                    e_rep=True
                    if(r<2*k-1):
                        top5e[r+2]=top5e[r]
                        top5e[r+1]=top5e[r-1]
                    top5e[r -1] = j
                    top5e[r] = e
                if c> top5c[r] and not c_rep :
                    c_rep = True
                    if(r<2*k-1):
                        top5c[r + 2] = top5c[r]
                        top5c[r + 1] = top5c[r - 1]
                    top5c[r - 1] = j
                    top5c[r] = c
                r=r+1
    #for income
    #top=income_append(p[0],top5e,top5c)
    #for iris
    top=iris_append(i,top5c,top5e)
    calc.append(top)
file.close
#for iris
output_iris_symmetry(calc)
#for income
#output_income_symmetry(calc)

