import pandas as pd
def getDensityKM2():
    gDKM2 = pd.read_csv('citys.csv',usecols=['City','Density KM2'])
    return gDKM2.head(10).dropna()