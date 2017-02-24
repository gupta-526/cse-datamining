#input: iris or income datasets
import csv
def distance_income(k):
    dat=[]
    trn=[]
    calc=[]
    header=["Trans. ID"]
    for i in range(1,k+1):
        header.append("ID")
        header.append("Symm")
        header.append("Class")
    with open("dataset/transformed_inc_test_file.csv") as file:
        with open("dataset/income_training.csv") as training:
            read=csv.reader(file)
            train=csv.reader(training)
            next(read)
            next(train)
            for row in train:
                q=row
                if not " ?" in q and not "?" in q:
                    for n in range(0, len(q)-1):
                        if n!=3:
                            q[n]=float(q[n])
                    trn.append(q)
            for row in read:
                p=row
                if not " ?" in p and not "?" in p:
                    for n in range(0, len(p)-1):
                        if n!=3:
                            p[n]=float(p[n])
                    dat.append(p)
        file.close()
        training.close()
    for i in range(0, len(dat)):
        p=dat[i]
        top5c=[]
        top5e=[]
        for s in range(0,3*k):
            top5e.append(-1)
            #top5e.append(100000)
        for j in range(0, len(trn)):
            q=trn[j]
            if j!=i:
                e=0
                for m in range(0, len(p)-1):
                    if m<len(p)-1 and m!=3:
                        e=e+abs(p[m]-q[m])
                e=(1/(len(p)-2))*e
                num=0
                denomp=0
                denomq=0
                for m in range(0,len(p)-1):
                    num=num+(p[m]*q[m])
                    denomp=denomp+p[m]*p[m]
                    denomq=denomq+q[m]*q[m]
                c=num/(denomp*denomq)
                e_rep = False
                c_rep = False
                seq=[]
                for x in range(0,3*k):
                    if x%3==0:
                        seq.append(x)
                # for r in seq:
                #     if e < top5e[r+1] and not e_rep:
                #         e_rep=True
                #         if(r<3*k-3):
                #             top5e[r + 3] = top5e[r]
                #             top5e[r + 4] = top5e[r + 1]
                #             top5e[r + 5] = top5e[r + 2]
                #         top5e[r] = j
                #         top5e[r + 1] = e
                #         top5e[r + 2] = q[-1]
                for r in seq:
                    if c> top5e[r + 1] and not c_rep:
                        c_rep = True
                        if (r < 3 * k - 3):
                            top5e[r + 3] = top5e[r]
                            top5e[r + 4] = top5e[r + 1]
                            top5e[r + 5] = top5e[r + 2]
                        top5e[r] = j
                        top5e[r + 1] = e
                        top5e[r + 2] = q[-1]
        top=[p[0]]
        top.append(top5e)
        #top.append(top5c)
        calc.append(top)
    outE=open("dataset/income_sym_euclidean.csv",'w')
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

def distance_iris(k):
    dat=[]
    trn=[]
    calc=[]
    header=["Trans. ID"]
    for i in range(1,k+1):
        header.append("ID")
        header.append("Symm")
        header.append("Class")
    with open("dataset/transformed_iris_test_file.csv") as file:
        with open("dataset/iris_training.csv") as training:
            read=csv.reader(file)
            train=csv.reader(training)
            next(read)
            next(train)
            for row in train:
                q=row
                if not " ?" in q and not "?" in q:
                    for n in range(0, len(q)-2):
                        if n!=3:
                            q[n]=float(q[n])
                    trn.append(q)
            for row in read:
                p=row
                if not " ?" in p and not "?" in p:
                    for n in range(0, len(p)-2):
                        if n!=3:
                            p[n]=float(p[n])
                    dat.append(p)
        file.close()
        training.close()
    for i in range(0, len(dat)):
        p=dat[i]
        top5c=[]
        top5e=[]
        for s in range(0,3*k):
            top5c.append(-1)
            top5e.append(100000)
        for j in range(0, len(trn)):
            q=trn[j]
            if j!=i:
                e=0
                for m in range(0, len(p)-3):
                   if m<len(p)-2:
                        e=e+abs(p[m]-q[m])
                e=(1/(len(p)-2))*e
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
        top=[i]
        top.append(top5e)
        #top.append(top5c)
        calc.append(top)
    outE=open("dataset/iris_sym_euclidean.csv",'w')
    #outC=open("dataset/iris_sym_cosine.csv","w")
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


def main():
    k=5
    distance_income(k)
    distance_iris(k)

main()