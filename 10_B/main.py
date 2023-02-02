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
    gPP = pp.getAllPopulation().replace({",":""},regex=True)


    X = list(gPP.iloc[:, 1])
    Y = list(gPP.iloc[:, 0])

    plt.pie(X, labels=Y, autopct="%0.1f %%")
    plt.axis("equal")
    # plt.legend()
    plt.title("Población")
    plt.show()

Population()

def DensityKM2():
    gDKM2 = dm2.getDensityM2().replace({",":""},regex=True)

    X = list(gDKM2.iloc[:, 1])
    Y = list(gDKM2.iloc[:, 0])

    plt.pie(X, labels=Y, autopct="%0.1f %%")
    plt.axis("equal")
    # plt.legend()
    plt.title("Densisdad por KM2")
    plt.show()

DensityKM2()

def DensityM2():
    gDM2 = dkm2.getDensityKM2().replace({",":""},regex=True)

    X = list(gDM2.iloc[:, 1])
    Y = list(gDM2.iloc[:, 0])

    plt.pie(X, labels=Y, autopct="%0.1f %%")
    plt.axis("equal")
    plt.title("Densidad por M2")
    # plt.legend()
    plt.show()

DensityM2()