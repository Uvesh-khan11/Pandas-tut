import pandas as pd 

df = pd.read_csv('./House.csv')
# new_df = df.dropna() # Note: By default, the dropna() method returns a new DataFrame, and will not change the original.
# df.dropna(inplace= True)
# Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.
# print(df.to_string())

# Replace Empty Values
# Another way of dealing with empty cells is to insert a new value instead.
# This way you do not have to delete entire rows just because of some empty cells.
# The fillna() method allows us to replace empty cells with a value:
# df.fillna(4,inplace=True) # This will insert 4 in null cells
# df[" Address    "].fillna(130, inplace = True)


# Replace Using Mean, Median, or Mode
# A common way to replace empty cells, is to calculate the mean, median or mode value of the column.
# Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:
x = df["Calories"].mean() # Mean = the average value (the sum of all values divided by number of values).
x = df["Calories"].median() # Median = the value in the middle, after you have sorted all values ascending.
x = df["Calories"].mode() # Mode = the value that appears most frequently.

df["Calories"].fillna(x, inplace = True)

