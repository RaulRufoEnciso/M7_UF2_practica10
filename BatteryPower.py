import pandas as pd
def getBatteryPower():
    gBP = pd.read_csv('test.csv',usecols=['id','battery_power'],nrows=10)
    return gBP;
