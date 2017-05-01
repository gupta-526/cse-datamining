import csv


def performance_rate(name):
    # 1 is eat, 0 is poisonous for mushrooms, 0 for benign, 1 for malignant
    matrix = {"True Positive": 0, "True Negative": 0, "False Positive": 0, "False Negative": 0}
    with open("Naive_Output/{0}.csv".format(name)) as table:
        read=csv.reader(table)
        next(read)
        for row in read:
            if float(row[1])== 0:
                if float(row[2]) == 0:
                    matrix["True Negative"]=matrix["True Negative"]+1
                elif float(row[2]) == 1:
                    matrix["False Negative"]=matrix["False Negative"]+1
            elif float(row[1]) == 1:
                if float(row[2]) == 1:
                    matrix["True Positive"]=matrix["True Positive"]+1
                elif float(row[2]) == 0:
                    matrix["False Positive"]=matrix["False Positive"]+1
    table.close()
    return matrix


def performance_rate_glass(name):
    # 1 is eat, 0 is poisonous for mushrooms, 0 for benign, 1 for malignant
    matrix = {"P1-A1":0, "P1-A2":0, "P1-A3":0, "P1-A4":0, "P1-A5":0, "P1-A6":0, "P1-A7":0,
              "P2-A1":0, "P2-A2":0, "P2-A3":0, "P2-A4":0, "P2-A5":0, "P2-A6":0, "P2-A7":0,
              "P3-A1":0, "P3-A2":0, "P3-A3":0, "P3-A4":0, "P3-A5":0, "P3-A6":0, "P3-A7":0,
              "P4-A1":0, "P4-A2":0, "P4-A3":0, "P4-A4":0, "P4-A5":0, "P4-A6":0, "P4-A7":0,
              "P5-A1":0, "P5-A2":0, "P5-A3":0, "P5-A4":0, "P5-A5":0, "P5-A6":0, "P5-A7":0,
              "P6-A1":0, "P6-A2":0, "P6-A3":0, "P6-A4":0, "P6-A5":0, "P6-A6":0, "P6-A7":0,
              "P7-A1":0, "P7-A2":0, "P7-A3":0, "P7-A4":0, "P7-A5":0, "P7-A6":0, "P7-A7":0}
    with open("Naive_Output/{0}.csv".format(name)) as table:
        read=csv.reader(table)
        next(read)
        for row in read:
            matrix["P{0}-A{0}".format(int(row[1]),int(row[2]))] = matrix["P{0}-A{0}".format(int(row[1]),int(row[2]))]+1
    table.close()
    return matrix


def performance_rate_posterior(threshold,name):
    matrix = {"True Positive": 0, "True Negative": 0, "False Positive": 0, "False Negative": 0}
    neg =0
    pos = 1
    with open("Naive_Output/{0}.csv".format(name)) as table:
        read=csv.reader(table)
        next(read)
        for row in read:
            if float(row[-1]) <threshold:
                if float(row[2]) == neg:
                    matrix["True Negative"]=matrix["True Negative"]+1
                if float(row[2]) == pos:
                    matrix["False Negative"]=matrix["False Positive"]+1
            if float(row[-1]) >=threshold:
                if float(row[2]) == pos:
                    matrix["True Positive"] = matrix["True Positive"] + 1
                if float(row[2]) == neg:
                    matrix["False Positive"] = matrix["False Negative"] + 1
    table.close()
    return matrix

def roc(name):
    thresholds=[.97,.95,.93,.81,.55,.28,.17,.15,.10,.03]
    table=[]
    for i in thresholds:
        matrix=performance_rate_posterior(i,name)
        tpr=matrix["True Positive"]/(matrix["True Positive"]+matrix["False Negative"])
        fpr=matrix["False Positive"]/(matrix["False Positive"]+matrix["True Negative"])
        table.append([i,tpr,fpr])
    return table

def precision(matrix):
    return matrix["True Positive"]/(matrix["True Positive"]+matrix["False Positive"])
def recall(matrix):
    return matrix["True Positive"]/(matrix["True Positive"]+matrix["False Negative"])

def f_measure(matrix):
    num=precision(matrix)*recall(matrix)
    denom=precision(matrix)+recall(matrix)
    return 2*num/denom

def main():
    cancer_matrix=performance_rate("breast_cancer")
    mush_matrix=performance_rate("mushrooms")
    print("cancer matrix")
    print(cancer_matrix)
    print("mush matrix")
    print(mush_matrix)
    print("mushroom roc")
    print(roc("mushrooms"))
    print("cancer roc")
    print(roc("breast_cancer"))
    print("f measure mushroom")
    print(f_measure(mush_matrix))
    print("precision mushroom")
    print(precision(mush_matrix))
    print("recall mushroom")
    print(recall(mush_matrix))
    print("f measure cancer")
    print(f_measure(cancer_matrix))
    print("precision cancer")
    print(precision(cancer_matrix))
    print("recall cancer")
    print(recall(cancer_matrix))
    glass_matrix=performance_rate_glass("glass")
    print("glass matrix")
    print(glass_matrix)

main()