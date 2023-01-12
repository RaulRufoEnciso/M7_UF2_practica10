import pandas as pd
def getClockSpeed():
    gCS = pd.read_csv('test.csv',usecols=['id','clock_speed'],nrows=10)
    return gCS;