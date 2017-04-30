import csv


def performance_rate_knn(name):
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
                    matrix["False Positive"]=matrix["False Positive"]+1
            elif float(row[1]) == 1:
                if float(row[2]) == 1:
                    matrix["True Positive"]=matrix["True Positive"]+1
                elif float(row[2]) == 0:
                    matrix["False Negative"]=matrix["False Negative"]+1
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
    cancer_matrix=performance_rate_knn("breast_cancer")
    mush_matrix=performance_rate_knn("mushrooms")
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
    print(f_measure(mush_matrix))
    print("precision cancer")
    print(precision(mush_matrix))
    print("recall cancer")
    print(recall(mush_matrix))


main()