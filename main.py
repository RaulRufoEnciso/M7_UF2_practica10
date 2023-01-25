import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
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
    gM = mp.getMegapixels()

    X = list(gM.iloc[:, 0])
    Y = list(gM.iloc[:, 1])

    plt.bar(X, Y, color="red")
    plt.title("MegaPixeles")
    plt.xlabel("Id Megapixeles")
    plt.ylabel("Megapixeles")
    plt.show()

MP()

def BP():
    gBP = bp.getBatteryPower()

    X = list(gBP.iloc[:, 0])
    Y = list(gBP.iloc[:, 1])

    plt.bar(X, Y, color="yellow")
    plt.title("Battery_Powder")
    plt.xlabel("Id Battery Powder")
    plt.ylabel("Battery Powder")
    plt.show()

BP()

def CS():
    gCS = cs.getClockSpeed()

    X = list(gCS.iloc[:, 0])
    Y = list(gCS.iloc[:, 1])

    plt.bar(X, Y, color="purple")
    plt.title("Clock_Speed")
    plt.xlabel("Id Clock_Speed")
    plt.ylabel("Clock_Speed")
    plt.show()

CS()
'''
def main():

    window = plt.figure()
    fig1 = window.add_subplot(2, 2, 1);
    fig2 = window.add_subplot(2, 2, 2);
    fig3 = window.add_subplot(2, 2, 3);

    fig1.plot(MP())
    fig2.plot(BP())
    fig3.plot(CS())
    plt.show()

main()
'''