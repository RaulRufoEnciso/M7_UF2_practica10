import pandas as pd
filas = 10
def getBatteryPower():
    gBP = pd.read_csv('test.csv',usecols=['id','battery_power'],nrows=filas)
    return gBP;

