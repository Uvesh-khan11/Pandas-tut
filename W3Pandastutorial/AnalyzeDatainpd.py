import pandas as pd

df = pd.read_csv('./House.csv')
# print(df.head(2))
# print(df.tail(2))
print(df.info()) # Print dtype and colums and other information of df