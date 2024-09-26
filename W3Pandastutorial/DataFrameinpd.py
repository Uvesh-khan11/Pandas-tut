import pandas as pd
# # What is A DataFrame : -
# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45],
}

#load data into a DataFrame object:
# df = pd.DataFrame(data)
# print(df) 

# Locate Row or find a row 
# Dataframe is like Table column and row , pandas use the loc to locate the row
# print(df.loc[0])
# print(df.loc[[0, 1]])

# You Can set Index also with your own
df = pd.DataFrame(data , index = ["A", "B", "C"])
print(df)
print(df.loc["A"]) # You can loc index also