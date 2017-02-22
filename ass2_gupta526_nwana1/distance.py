#input: iris or income
import csv
dat=[]
calc=[]
#change if needed, where k is number of closest tuples
k=5
header=["Trans. ID"]
for i in range(1,k+1):
    header.append("ID")
    header.append("Symm")
    header.append("Class")
#for iris
with open("dataset/iris_test.csv") as file:
#for income
#with open("dataset/transformed_file.csv") as file:
    read=csv.reader(file)
    next(read)
    for row in read:
        p=row
        #next line used for iris only. comment out if for income
        #p=p[0:4]
        if not " ?" in p and not "?" in p:
            for n in range(0, len(p)-1):
                p[n]=float(p[n])
            dat.append(p)
for i in range(0, len(dat)):
    p=dat[i]
    top5c=[]
    top5e=[]
    for s in range(0,3*k):
        top5c.append(-1)
        top5e.append(100000)
    for j in range(0, len(dat)):
        q=dat[j]
        if j!=i:
            e=0
            for m in range(0, len(p)-1):
                e=e+abs(p[m]-q[m])
            e=(1/len(p))*e
            num=0
            denomp=0
            denomq=0
            # for m in range(0,len(p)-1):
            #     num=num+(p[m]*q[m])
            #     denomp=denomp+p[m]*p[m]
            #     denomq=denomq+q[m]*q[m]
            # c=num/(denomp*denomq)
            e_rep = False
            c_rep = False
            seq=[]
            for x in range(0,3*k):
                if x%3==0:
                    seq.append(x)
            for r in seq:
                if e < top5e[r+1] and not e_rep:
                    e_rep=True
                    if(r<3*k-3):
                        top5e[r + 3] = top5e[r]
                        top5e[r + 4] = top5e[r + 1]
                        top5e[r + 5] = top5e[r + 2]
                    top5e[r] = j
                    top5e[r + 1] = e
                    top5e[r + 2] = q[-1]
                # if  c> top5c[r] and not c_rep :
                #     c_rep = True
                #     if(r<2*k-1):
                #         top5c[r + 2] = top5c[r]
                #         top5c[r + 1] = top5c[r - 1]
                #     top5c[r - 1] = j
                #     top5c[r] = c
                #r=r+1
    #for iris
    top=[i]
    #for income, or data with own ID column
    #top=[p[0]]
    top.append(top5e)
    #top.append(top5c)
    calc.append(top)
file.close
#for iris
outE=open("dataset/iris_sym_euclidean.csv",'w')
#outC=open("dataset/iris_sym_cosine.csv","w")
#for income
#outE=open("dataset/income_sym_euclidean.csv",'w')
#outC=open("dataset/income_sym_cosine.csv","w")
wrE = csv.writer(outE, quoting=csv.QUOTE_ALL)
#wrC= csv.writer(outC, quoting=csv.QUOTE_ALL)
wrE.writerow(header)
#wrC.writerow(header)
for i in range(0,len(calc)):
    row=calc[i]
    id=row[0]
    e=row[1]
    #c=row[2]
    #rowC=[id]
    rowE=[id]
    for i in range(0,len(e)):
        #rowC.append(c[i])
        rowE.append(e[i])
    #wrC.writerow(rowC)
    wrE.writerow(rowE)
outE.close()
#outC.close()
