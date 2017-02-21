def eval_performance(list):
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