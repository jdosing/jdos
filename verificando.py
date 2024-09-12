import pandas as pd
import numpy as np 
import openpyxl

df = pd.read_excel('./Ventas_Olimpica_2023.xlsx',usecols=['CodProducto','UNIDVendidas','ValorUnidad']) #estoy leyendo un docuemento de excel, y solo viendo 3 columnas

unidvendidas = df.groupby('CodProducto')['UNIDVendidas'].sum() 
print(type(unidvendidas))
unidvendidas = pd.DataFrame(unidvendidas)#debo pasar a dataframe para que me permita seguir agregando...
#sumo las unidades vendidas por item, haciendo una reduccion con respepto a codigo de producto
unidvendidas['Valor_Unidad'] = df.groupby('CodProducto')['ValorUnidad'].first()
#agrego una columna con el primer valor encontrado por item
unidvendidas['Venta_producto'] = unidvendidas['Valor_Unidad']*unidvendidas['UNIDVendidas']
#calculo la venta total por producto, agregando una columna


venta_total = pd.DataFrame(unidvendidas) #cargo la data 
venta_total = venta_total.drop(columns=['UNIDVendidas','Valor_Unidad'])
total = venta_total['Venta_producto'].sum()
#limpio almaceno y sumo en una variable para tener listo el total
newfila = pd.DataFrame({'Venta_producto':[(total)]})
#creo una nueva fila y ubico el total 
venta_total = pd.concat([venta_total,newfila])
#agrego al dataframe 

filters = pd.read_excel('./Ventas_Olimpica_2023.xlsx')
filters['VentaXproducto'] = filters['UNIDVendidas']*filters['ValorUnidad']



with pd.ExcelWriter('./consolidado.xlsx') as writer:
    filters.to_excel(writer,sheet_name='filtros',index=False)
    unidvendidas.to_excel(writer,sheet_name='ventasProductos'),
    venta_total.to_excel(writer,sheet_name='VentaTotal'),    
#me permite crear nuevas hojas dentro del mismo archiuo


wb = openpyxl.load_workbook('./consolidado.xlsx')
ws = wb.active

# Agregar filtros
ws.auto_filter.ref = ws.dimensions

# Guardar el archivo con los filtros habilitados
wb.save('./consolidado.xlsx')

print(filters)
print(type(filters))