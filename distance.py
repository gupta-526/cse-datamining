#input: iris or income
import csv
dat=[]
calc=[]
#change if needed
k=5
header=["Trans. ID"]
for i in range(1,k+1):
    header.append("ID")
    header.append("Symm")



#iris
with open("iris_test.csv") as file:
    read=csv.reader(file)
    next(read)
    for row in read:
        p=row
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
        top5c.append(0)
        top5e.append(0)
    for j in range(0, len(dat)):
        q=dat[j]
        if j!=i:
            e=0
            for m in range(0, len(p)):
                e=e+abs(p[m]-q[m])
            e=(1/len(p))*e
            num=0
            denomp=0
            denomq=0
            for m in range(0,len(p)):
                num=num+(p[m]*q[m])
                denomp=denomp+p[m]
                denomq=denomq+q[m]
            c=num/(denomp*denomq)
            e_rep = False
            c_rep = False
            seq=[]
            for x in range(1,2*k):
                if x%2!=0:
                    seq.append(x)
            for r in seq:
                if e > top5e[r] and not e_rep:
                    e_rep=True
                    if(r<9):
                        top5e[r+2]=top5e[r]
                        top5e[r+1]=top5e[r-1]
                    top5e[r -1] = j
                    top5e[r] = e
                if  c> top5c[r] and not c_rep :
                    c_rep=True
                    if(r<9):
                        top5c[r + 2] = top5c[r]
                        top5c[r + 1] = top5c[r - 1]
                    top5c[r - 1] = j
                    top5c[r] = c
                r=r+1
    top=[i]
    top.append(top5c)
    top.append(top5e)
    calc.append(top)
file.close
outE=open("iris_sym_euclidean.csv",'w')
outC=open("iris_sym_cosine.csv","w")
wrE = csv.writer(outE, quoting=csv.QUOTE_ALL)
wrC= csv.writer(outC, quoting=csv.QUOTE_ALL)
wrE.writerow(header)
wrC.writerow(header)
for i in range(0,len(calc)):
    row=calc[i]
    id=row[0]
    e=row[1]
    c=row[2]
    rowC=[id]
    rowE=[id]
    for i in range(0,len(e)):
        rowC.append(c[i])
        rowE.append(e[i])
    wrC.writerow(rowC)
    wrE.writerow(rowE)
outE.close()
outC.close()

#income
dat=[]
calc=[]
#15 variables
with open("transformed_file.csv") as file:
    read=csv.reader(file)
    next(read)
    for row in read:
        p=row
        if not " ?" in p and not "?" in p:
            for n in range(0, len(p)):
                p[n]=float(p[n])
            dat.append(p)
for i in range(0, len(dat)):
    p=dat[i]
    top5e =[]
    top5c=[]
    for s in range(0,2*k):
        top5c.append(0)
        top5e.append(0)
    for j in range(0, len(dat)):
        q=dat[j]
        if j!=i:
            e=0
            for m in range(0, len(p)):
                e=e+abs(p[m]-q[m])
            e=(1/len(p))*e
            num=0
            denomp=0
            denomq=0
            for m in range(0,len(p)):
                num=num+(p[m]*q[m])
                denomp=denomp+p[m]
                denomq=denomq+q[m]
            c=num/(denomp*denomq)
            e_rep = False
            c_rep = False
            seq = []
            for x in range(1, 2 * k):
                if x % 2 != 0:
                    seq.append(x)
            for r in seq:
                if e>top5e[r] and not e_rep:
                    e_rep=True
                    if(r<9):
                        top5e[r+2]=top5e[r]
                        top5e[r+1]=top5e[r-1]
                    top5e[r -1] = j
                    top5e[r] = e
                if c>top5c[r] and not c_rep :
                    c_rep=True
                    if(r<9):
                        top5c[r + 2] = top5c[r]
                        top5c[r + 1] = top5c[r - 1]
                    top5c[r - 1] = j
                    top5c[r] = c
                r=r+1

    top=[p[0]]
    top.append(top5c)
    top.append(top5e)
    calc.append(top)
file.close()
outE=open("income_sym_euclidean.csv",'w')
outC=open("income_sym_cosine.csv","w")
wrE = csv.writer(outE, quoting=csv.QUOTE_ALL)
wrC= csv.writer(outC, quoting=csv.QUOTE_ALL)
wrE.writerow(header)
wrC.writerow(header)
for i in range(0,len(calc)):
    row=calc[i]
    id=row[0]
    e=row[1]
    c=row[2]
    rowC=[id]
    rowE=[id]
    for i in range(0,len(e)):
        rowC.append(c[i])
        rowE.append(e[i])
    wrC.writerow(rowC)
    wrE.writerow(rowE)
outE.close()
outC.close()