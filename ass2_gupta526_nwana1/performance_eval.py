import csv


def inc_performance_rate_knn():
    matrix = {"True Positive": 0, "True Negative": 0, "False Positive": 0, "False Negative": 0}
    neg = [" <=50K", " <=50K ", "<=50K ", "<=50K"]
    pos = [">50K", ">50K ", " >50K", " >50K "]
    with open("output/knn_result_income.csv") as table:
        #positive is over 50k, negative is under 50k
        read=csv.reader(table)
        next(read)
        for row in read:
            if row[1] in neg:
                if row[2] in neg:
                    matrix["True Negative"]=matrix["True Negative"]+1
                if row[2] in pos:
                    matrix["False Positive"]=matrix["False Positive"]+1
            if row[1] in pos:
                if row[2] in pos:
                    matrix["True Positive"]=matrix["True Positive"]+1
                if row[2] in neg:
                    matrix["False Negative"]=matrix["False Negative"]+1
    table.close()
    return matrix

def iris_performance_rate_knn():
    #predicted, actual
    matrix = {"Setosa| Virginica": 0,"Setosa| Setosa": 0,"Setosa| Versicolor": 0,
              "Virginica| Virginica": 0,"Virginica| Setosa": 0,"Virginica| Versicolor": 0,
              "Versicolor| Virginica": 0, "Versicolor| Setosa": 0, "Versicolor| Versicolor": 0,}
    with open("output/knn_result_iris.csv") as table:
        read=csv.reader(table)
        next(read)
        for row in read:
            if row[1]=="Iris-setosa":
                if row[2] =="Iris-setosa":
                    matrix["Setosa| Setosa"]=matrix["Setosa| Setosa"]+1
                if row[2] == "Iris-versicolor":
                    matrix["Setosa: Versicolor"]=matrix["Setosa: Versicolor"]+1
                if row[2] == "Iris-virginica":
                    matrix["Setosa| Virginica"] = matrix["Setosa| Virginica"] + 1
            if row[1]=="Iris-versicolor":
                if row[2] =="Iris-setosa":
                    matrix["Versicolor| Setosa"]=matrix["Versicolor| Setosa"]+1
                if row[2] == "Iris-versicolor":
                    matrix["Versicolor| Versicolor"]=matrix["Versicolor| Versicolor"]+1
                if row[2] == "Iris-virginica":
                    matrix["Versicolor| Virginica"] = matrix["Versicolor| Virginica"] + 1
            if row[1]=="Iris-virginica":
                if row[2] =="Iris-setosa":
                    matrix["Virginica| Setosa"]=matrix["Virginica| Setosa"]+1
                if row[2] == "Iris-versicolor":
                    matrix["Virginica| Versicolor"]=matrix["Virginica| Versicolor"]+1
                if row[2] == "Iris-virginica":
                    matrix["Virginica| Virginica"] = matrix["Virginica| Virginica"] + 1
    table.close()
    return matrix

def performance_rate_posterior(threshold):
    matrix = {"True Positive": 0, "True Negative": 0, "False Positive": 0, "False Negative": 0}
    neg = [" <=50K", " <=50K ", "<=50K ", "<=50K"]
    pos = [">50K", ">50K ", " >50K", " >50K "]
    with open("output/knn_result_income.csv") as table:
        read=csv.reader(table)
        next(read)
        for row in read:
            if float(row[-1]) <threshold:
                if row[2] in neg:
                    matrix["True Negative"]=matrix["True Negative"]+1
                if row[2] in pos:
                    matrix["False Negative"]=matrix["False Positive"]+1
            if float(row[-1]) >=threshold:
                if row[2] in pos:
                    matrix["True Positive"] = matrix["True Positive"] + 1
                if row[2] in neg:
                    matrix["False Positive"] = matrix["False Negative"] + 1
    table.close()
    return matrix

def roc():
    thresholds=[.97,.95,.93,.81,.55,.28,.17,.15,.10,.03]
    table=[]
    for i in thresholds:
        matrix=performance_rate_posterior(i)
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
    inc_matrix=inc_performance_rate_knn()
    iris_matrix=iris_performance_rate_knn()
    print("iris matrix")
    print(iris_matrix)
    print("inc matrix")
    print(inc_matrix)
    print("roc")
    print(roc())
    print("f measure inc")
    print(f_measure(inc_matrix))
    print("precision")
    print(precision(inc_matrix))
    print("recall")
    print(recall(inc_matrix))


main()