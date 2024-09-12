import pandas as pd
import numpy as np 

data = pd.read_excel('.\Ventas_Olimpica_2023.xlsx')
dataset = pd.Series(data.to_numpy().tolist())

temp = 0

for i in range(len(dataset)):
    if dataset[i][0]=='SAOVia_40':
        temp += dataset[i][5]*dataset[i][6] 
print(temp)       

"""data['Total_Productos'] = data['UNIDVendidas']*data['ValorUnidad']

with pd.ExcelWriter('.\consolidado.xlsx') as writer:
    dataset.to_excel(writer,sheet_name='Ventas')
"""
#print(dataset[i][j]*dataset[i][j])