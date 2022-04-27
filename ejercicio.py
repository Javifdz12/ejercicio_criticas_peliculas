import pandas as pd
import math
list1=[0,1,2,3,4,5]
list2=[40,96,133,145,99,40]

dict1={"opinion(Xi)":list1,"cantidad_votantes(Ni)":list2}
dataframe=pd.DataFrame(dict1)
dataframe["producto(Ni*Xi)"]=dataframe["opinion(Xi)"]*dataframe["cantidad_votantes(Ni)"]
x=dataframe["producto(Ni*Xi)"].sum()
observaciones=dataframe["cantidad_votantes(Ni)"].sum()
media=x/observaciones
dataframe["Ni*(Xi-media)^2"] = dataframe["cantidad_votantes(Ni)"] * ((dataframe["opinion(Xi)"] - media)*(dataframe["opinion(Xi)"] - media))
varianza=dataframe["Ni*(Xi-media)^2"].sum()/observaciones
desviacion_tipica=math.sqrt(varianza)
print(dataframe)

a=media-(3*desviacion_tipica)
b=media+(3*desviacion_tipica)
dataframe2=dataframe.loc[dataframe["opinion(Xi)"]<=3]
dataframe2=dataframe2.loc[dataframe["opinion(Xi)"]>=1]
z=dataframe2["cantidad_votantes(Ni)"].sum()
probabilidad=(z/observaciones)*100
print(dataframe2)
print(f"[{a},{b}]")
print(probabilidad)

# en [1,3] estan el 67.63% de las observaciones, en [-0.18,5.21] y [-1.53,6.56] estan evidentemente el 100% de las observaciones