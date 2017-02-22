def performance_rate(list,threshold):
    #call the classifier function with the given threshold
    classifier(threshold)
    #positive is over 50k, negative is under 50k
    matrix = {"True Positive": 0, "True Negative": 0, "False Positive": 0, "False Negative": 0}
    neg=[" <=50K"," <=50K ","<=50K ","<=50K"]
    pos=[">50K",">50K "," >50K", " >50K "]
    for i in range(0, len(list)):
        trans=list[i]
        if trans[1] in neg:
            if trans[2] in neg:
                matrix["True Negative"]=matrix["True Negative"]+1
            if trans[2] in pos:
                matrix["False Positive"]=matrix["False Positive"]+1
        if trans[1] in pos:
            if trans[2] in pos:
                matrix["True Positive"]=matrix["True Positive"]+1
            if trans[2] in neg:
                matrix["False Negative"]=matrix["False Negative"]+1
    return matrix

#slide 96
#need threshold of cutoff and tpr and fpr
def roc(list):
    #dummy numbers for now
    thresholds=[1,2,3,4,5,6]
    table=[]
    for i in thresholds:
        matrix=performance_rate(list,thresholds[i])
        table.append([thresholds[i],matrix["True Positive"],matrix["False Positive"]])
    return table

def precision(matrix):
    return matrix["True Positive"]/(matrix["True Positive"]+matrix["False Positive"])

def recall(matrix):
    return matrix["True Positive"]/(matrix["True Positive"]+matrix["False Negative"])

def f_measure(matrix):
    num=precision(matrix)*recall(matrix)
    denom=precision(matrix)+recall(matrix)
    return 2*num/denom

#first dictionary is age probabilities, second is workclass ect
#all from training data
probabilities=[{0:(1/79),1:(1/79),2:(1/79)},]

#where e is an iterable tuple (list)
def posterior(e):
    num=0
    denom=probability[e]
    for i in range(0,len(e)):
        #where you look in the list at dictionary i, and in dictionary i, get the probability
        #of the value in e[i]
        num=num*probabilities[i[e[i]]]
    num=num*(18/79)
    return num/denom
