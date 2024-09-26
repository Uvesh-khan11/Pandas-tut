import pandas as pd
# Read CSV Files
# A simple way to store big data sets is to use CSV files (comma separated files).
# CSV files contains plain text and is a well know format that can be read by everyone including Pandas.
# In our examples we will be using a CSV file called 'data.csv'.
df = pd.read_csv(' ./House.csv')
# print(df.to_string())
# pd.options.display.max_rows = 9999 # Cause print(df)only print