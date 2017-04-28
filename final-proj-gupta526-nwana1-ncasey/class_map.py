import csv, pandas as pd, numpy as np
def mushroom_transform():
    name="mushrooms"
    mush = pd.read_csv("Dataset/{0}.csv".format(name))
    mush['class'] = mush['class'].map({'p': 0, 'e': 1})
    mush['cap-shape']=mush['cap-shape'].map({'x':0,'b':1,'s':2,'f':3,'k':4,'c':5})
    mush['cap-surface']=mush['cap-surface'].map({'s':0,'y':1,'f':2,'g':3})
    mush['cap-color']=mush['cap-color'].map({'n':0,'y':1,'w':2,'g':3,'e':4,'p':5,'b':6,'u':7,'c':8,'r':9})
    mush['bruises']=mush['bruises'].map({'f':0,'t':1})
    mush['odor']=mush['odor'].map({'p':0,'a':1,'l':2,'n':3,'f':4,'c':5,'y':6,'s':7,'m':8})
    mush['gill-attachment']=mush['gill-attachment'].map({'f':0,'a':1})
    mush['gill-spacing']=mush['gill-spacing'].map({'c':0,'w':1})
    mush['gill-size']=mush['gill-size'].map({'n':0,'b':1})
    mush['gill-color']=mush['gill-color'].map({'k':0,'n':1,'g':2,'p':3,'w':4,'h':5,'u':6,'e':7,'b':8,'r':9,'y':10,'o':11})
    mush['stalk-surface-below-ring']=mush['stalk-surface-below-ring'].map({'s':0,'f':1,'y':2,'k':3})
    mush['stalk-color-above-ring']=mush['stalk-color-above-ring'].map({'w':0,'g':1,'p':2,'n':3,'b':4,'e':5,'o':6,'c':7,'y':8})
    mush['stalk-color-below-ring']=mush['stalk-color-below-ring'].map({'w':0,'p':1,'g':2,'b':3,'n':4,'e':5,'y':6,'o':7,'c':8})
    mush['veil-type']=mush['veil-type'].map({'p':0})
    mush['veil-color']=mush['veil-color'].map({'w':0,'n':1,'o':2,'y':3})
    mush['ring-number']=mush['ring-number'].map({'o':0,'t':1,'n':2})
    mush['ring-type']=mush['ring-type'].map({'w':0,'g':1,'p':2,'n':3,'b':4,'e':5,'o':6,'c':7,'y':8})
    mush['spore-print-color']=mush['spore-print-color'].map({'k':0,'n':1,'u':2,'h':3,'w':4,'r':5,'o':6,'y':7,'b':8})
    mush['population']=mush['population'].map({'s':0,'n':1,'a':2,'v':3,'y':4,'c':5})
    mush['habitat']=mush['habitat'].map({'u':0,'g':1,'m':2,'d':3,'p':4,'w':5,'l':6})
    mush['stalk-root']=mush['stalk-root'].map({'e':0,'c':1,'b':2,'r':3,'?':4})
    mush['stalk-shape']=mush['stalk-shape'].map({'e':0,'t':1})
    mush['stalk-surface-above-ring']=mush['stalk-surface-above-ring'].map({'s':0,'f':1,'y':2,'k':3})
    mush.to_csv("Dataset/{0}_binary.csv".format(name))

def cancer_transform():
    name="breast_cancer"
    cancer=pd.read_csv("Dataset/{0}.csv".format(name))
    cancer['class']=cancer['class'].map({'M':1, 'B':0})
    cancer.to_csv("Dataset/{0}_binary.csv".format(name))


def main():
    mushroom_transform()
    cancer_transform()

main()