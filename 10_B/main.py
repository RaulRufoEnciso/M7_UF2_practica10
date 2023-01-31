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

    X = list(gPP.iloc[:, 1])
    Y = list(gPP.iloc[:, 0])

    plt.pie(X, labels=Y, autopct="%0.1f %%")
    plt.axis("equal")
    plt.show()

Population()

def DensityKM2():
    gDKM2 = dm2.getDensityM2()

    X = list(gDKM2.iloc[:, 0])
    Y = list(gDKM2.iloc[:, 1])

    plt.pie(X, labels=Y, autopct="%0.1f %%")
    plt.axis("equal")
    plt.show()

DensityKM2()

def DensityM2():
    gDM2 = dkm2.getDensityKM2()

    X = list(gDM2.iloc[:, 0])
    Y = list(gDM2.iloc[:, 1])

    plt.pie(X, labels=Y, autopct="%0.1f %%")
    plt.axis("equal")
    plt.show()

DensityM2()