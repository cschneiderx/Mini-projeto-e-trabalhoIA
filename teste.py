import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
dataset = pd.read_csv('hotel_bookings.csv', sep=',', index_col=0)

#emJulho = dataset[dataset['arrival_date_month'] =='July']
#print(emJulho)
dataset.isnull()
print(dataset.head(1))