import pandas as pd
def getMegapixels():
    gM = pd.read_csv('test.csv',usecols=['id','px_width'],nrows=10)
    return gM;