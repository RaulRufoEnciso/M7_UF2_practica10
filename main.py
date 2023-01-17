import matplotlib.pyplot as plt
import pandas as pd
import BatteryPower as bp
import ClockSpeed as cs
import Megapixels as mp

print("----------------------")
print(cs.getClockSpeed())
print("----------------------")
print(bp.getBatteryPower())
print("----------------------")
print(mp.getMegapixels())
def MP():
    gM = pd.read_csv('test.csv', usecols=['id', 'px_width'], nrows=10)

    X = list(gM.iloc[:,0])
    Y = list(gM.iloc[:, 1])

    plt.bar(X,Y, color="red")
    plt.title("MegaPixeles")
    plt.xlabel("Id Megapixeles")
    plt.ylabel("Megapixeles")
    plt.show()

MP()

def BP():
    gBP = pd.read_csv('test.csv',usecols=['id','battery_power'],nrows=10)

    X = list(gBP.iloc[:,0])
    Y = list(gBP.iloc[:, 1])

    plt.bar(X,Y, color="yellow")
    plt.title("Battery_Powder")
    plt.xlabel("Id Battery Powder")
    plt.ylabel("Battery Powder")
    plt.show()

BP()

def CS():
    gCS = pd.read_csv('test.csv',usecols=['id','clock_speed'],nrows=10)

    X = list(gCS.iloc[:,0])
    Y = list(gCS.iloc[:, 1])

    plt.bar(X,Y, color="purple")
    plt.title("Clock_Speed")
    plt.xlabel("Id Clock_Speed")
    plt.ylabel("Clock_Speed")
    plt.show()

CS()