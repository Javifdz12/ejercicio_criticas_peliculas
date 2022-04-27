import pandas as pd
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
print(dataframe)

dataframe2=dataframe.loc[dataframe["opinion(Xi)"]<=5]
dataframe2=dataframe2.loc[dataframe["opinion(Xi)"]>=1]
z=dataframe2["cantidad_votantes(Ni)"].sum()
probabilidad=(z/observaciones)*100
print(dataframe2)
print(probabilidad)