import pandas as pd
import numpy as np
# How to creeate a DataFrame in Python Pandas

# df = pd.DataFrame() # Null DataFrame
print(df)

# df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]) # DataFrame with columns and values
# print(df)
# print(df.head(2)) # head will print upper rows of a csv file or df
# print(df.tail(2)) # tail will print lower rows of a csv file or df
# df.columns = ['A', 'B', 'C'] # Set the columns names and you can directly access it without braces
# print(df)

# df = pd.read_csv('House.csv') # Read csv
# print(df.to_string()) # Print it in the string format

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}
df = pd.DataFrame(data)
df.to_csv("temp.csv")