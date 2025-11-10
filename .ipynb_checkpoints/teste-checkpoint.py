import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
dataset = pd.read_csv('hotel_bookings.csv', sep=';', index_col=0)

dataset