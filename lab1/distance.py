#input: iris or income

#iris
import csv
dat=[]
calc=[]
header=["ID","1st Match ID","Symm.","2nd Match ID","Symm.","3rd Match ID","Symm.","4th Match ID","Symm.","5th Match ID","Symm."]
with open("iris_test.csv") as iris:
    read=csv.reader(iris)
    next(read)
    for row in read:
        p=next(read)
        p=p[0:4]
        for i in range(0, len(p)):
            p[i]=float(p[i])
        dat.append(p)
for i in range(0, len(dat)):
    p=dat[i]
    top5e =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    top5c=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for j in range(0, len(dat)):
        q=dat[j]
        if j!=i:
            e=0
            for m in range(0, len(p)):
                e=e+abs(p[m]-q[m])
            e=.25*e
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
            for k in (1,3,5,7,9):
                if e>top5e[k] and not e_rep:
                    e_rep=True
                    if(k<9):
                        top5e[k+2]=top5e[k]
                        top5e[k+1]=top5e[k-1]
                    top5e[k -1] = j
                    top5e[k] = e
                if c>top5c[k] and not c_rep :
                    c_rep=True
                    if(k<9):
                        top5c[k + 2] = top5c[k]
                        top5c[k + 1] = top5c[k - 1]
                    top5c[k - 1] = j
                    top5c[k] = c
    top=[i]
    top.append(top5c)
    top.append(top5e)
    calc.append(top)
iris.close
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
with open("transformed_file.csv") as income:
    read=csv.reader(income)
    next(read)
    for row in read:
        p=row
        p=p[0:4]+p[5:16]
        if p[14]== " <=50K":
            p[14]=1
        else:
            p[14]=2
        if not " ?" in p and not "?" in p:
            for i in range(0, len(p)-1):
                p[i]=float(p[i])
            dat.append(p)
for i in range(0, len(dat)):
    p=dat[i]
    top5e =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    top5c=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for j in range(0, len(dat)):
        q=dat[j]
        if j!=i:
            e=0
            for m in range(0, len(p)):
                e=e+abs(p[m]-q[m])
            e=.25*e
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
            for k in (1,3,5,7,9):
                if e>top5e[k] and not e_rep:
                    e_rep=True
                    if(k<9):
                        top5e[k+2]=top5e[k]
                        top5e[k+1]=top5e[k-1]
                    top5e[k -1] = q[0]
                    top5e[k] = e
                if c>top5c[k] and not c_rep :
                    c_rep=True
                    if(k<9):
                        top5c[k + 2] = top5c[k]
                        top5c[k + 1] = top5c[k - 1]
                    top5c[k - 1] = q[0]
                    top5c[k] = c
    top=[p[0]]
    top.append(top5c)
    top.append(top5e)
    calc.append(top)
income.close()
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