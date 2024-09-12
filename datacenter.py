import pandas as pd 

data = pd.read_excel('./Ventas_Olimpica_2023.xlsx')
f_inicio = '1/1/2023'
f_fin = '31/3/2023'
datafil = data.query('Fecha>=@f_inicio and Fecha<= @f_fin')




with pd.ExcelWriter('./consolidado.xlsx') as writer:
    datafil.to_excel(writer,sheet_name='filtros',index=False)
    #unidvendidas.to_excel(writer,sheet_name='ventasProductos'),
    #venta_total.to_excel(writer,sheet_name='VentaTotal'),    
#me permite crear nuevas hojas dentro del mismo archiuo