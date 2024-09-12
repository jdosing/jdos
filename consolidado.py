#Luisa, desea calcular las ventas por producto del primer trimestre del año 2023, 
# para lo cual le proporciona una tabla en Excel que contiene los datos respectivos, 
# adicional requiere del total de ventas por productos, tanto de la cantidad de productos vendidos, 
# así, como el total de ventas en pesos, Luisa, 
# solicita que en la presentación del reporte se puedan hacer filtros por mes de ventas y tienda.
#Usted, como Ingeniero de Sistemas, 
# resuelve solucionarle a Luisa, procesando el reporte desde Python, 
# a lo que la joven compañera da su visto de aceptación y 
# le agradece por su gran apoyo y la forma en que decide solucionarlo.

import pandas as pd
import numpy as np 
data = [
    
]

df_products = pd.read_excel(r'./Ventas_Olimpica_2023.xlsx' ,usecols=['CodProducto'])
df_products = df_products.drop_duplicates
df_venta = pd.read_excel(r'./Ventas_Olimpica_2023.xlsx' ,usecols=['CodProducto','UNIDVendidas'])
df_venta = df_venta.groupby('CodProducto')['UNIDVendidas'].sum()
df_ventaMc = df_venta.drop(['CodProducto'])
df_ventaMp = df_venta.drop(['UNIDVendidas'])
data = pd.DataFrame(data)
data['Plu_Productos']= df_products
data['Uni_Vendidas']=df_ventaMc
data['Precio']=df_ventaMp

print(data)
dfVunit =  pd.read_excel(r'./Ventas_Olimpica_2023.xlsx' ,usecols=['CodProducto','ValorUnidad'])
dfVunit = dfVunit.groupby('CodProducto')['ValorUnidad'].first()
dfVunit = dfVunit.drop(columns=['CodProducto'])
#voy a reducir con respecto a codigo el valor por unidad
dfproduct = pd.read_excel(r'./Ventas_Olimpica_2023.xlsx' ,usecols=['CodProducto','UNIDVendidas'])
dfproduct = dfproduct.groupby('CodProducto')['UNIDVendidas'].sum()
#voy a reducir sumando con respecto a codigo las unidades vendidas
dfproduct['ValUnitario'] = dfVunit
dfproduct.to_excel(r'./consolidado.xlsx')



df_valores = df_valores.drop(columns=['CodProducto'])