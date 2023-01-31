import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import Population as pp
import DensityCityM2 as dm2
import DensityCityKm2 as dkm2

print("----------------------")
print(pp.getAllPopulation())
print("----------------------")
print(dm2.getDensityM2())
print("----------------------")
print(dkm2.getDensityKM2())
def Population():
    gPP = pp.getAllPopulation()

    X = list(gPP.iloc[:, 0])
    Y = list(gPP.iloc[:, 1])

    plt.bar(X, Y, color="red")
    plt.title("MegaPixeles")
    plt.xlabel("Id Megapixeles")
    plt.ylabel("Megapixeles")
    plt.show()

Population()

def DensityKM2():
    gDKM2 = dm2.getDensityM2()

    X = list(gDKM2.iloc[:, 0])
    Y = list(gDKM2.iloc[:, 1])

    plt.bar(X, Y, color="yellow")
    plt.title("Battery_Powder")
    plt.xlabel("Id Battery Powder")
    plt.ylabel("Battery Powder")
    plt.show()

DensityKM2()

def DensityM2():
    gDM2 = dkm2.getDensityKM2()

    X = list(gDM2.iloc[:, 0])
    Y = list(gDM2.iloc[:, 1])

    plt.bar(X, Y, color="purple")
    plt.title("Clock_Speed")
    plt.xlabel("Id Clock_Speed")
    plt.ylabel("Clock_Speed")
    plt.show()

DensityM2()