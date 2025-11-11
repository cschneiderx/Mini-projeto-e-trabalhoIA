import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
dataset = pd.read_csv('hotel_bookings.csv', sep=',', index_col= None)

#emJulho = dataset[dataset['arrival_date_month'] =='July']
#print(emJulho)
#if dataset.isna() == True:
 #   print("a")

print(dataset.isna().sum())
##Company
#testeAgent = dataset['agent']
#print(testeAgent)

#testeCompany = dataset['company']
#print(testeCompany)
#linhas_com_nulos_country = dataset["country"]
#linhas_com_nulos_country = dataset[dataset["country"].isnull()]
#print(linhas_com_nulos_country)

linhas_com_nulos_children = dataset[dataset["children"].isnull()]
print(linhas_com_nulos_children)
