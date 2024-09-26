import pandas as pd
import numpy as np
# How to creeate a DataFrame in Python Pandas

# df = pd.DataFrame() # Null DataFrame
# print(df)

# df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]) # DataFrame with columns and values
# print(df)
# print(df.head(2)) # head will print upper rows of a csv file or df
# print(df.tail(2)) # tail will print lower rows of a csv file or df
# df.columns = ['A', 'B', 'C'] # Set the columns names and you can directly access it without braces
# print(df)

df = pd.read_csv('House.csv') # Read csv
print(df.to_string()) # Print it in the string format