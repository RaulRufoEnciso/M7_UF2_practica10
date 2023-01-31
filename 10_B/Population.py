import pandas as pd
def getAllPopulation():
    gAP = pd.read_csv('citys.csv',usecols=['City','Population'])
    return gAP.head(10)
print(getAllPopulation())