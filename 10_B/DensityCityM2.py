import pandas as pd
def getDensityM2():
    gDM2 = pd.read_csv('citys.csv',usecols=['City','Density  M2'])
    return gDM2.head(10).dropna()