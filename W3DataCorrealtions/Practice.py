import pandas as pd
# Finding Relationships
# A great aspect of the Pandas module is the corr() method.
# The corr() method calculates the relationship between each column in your data set.
# The examples in this page uses a CSV file called: 'data.csv'.
df = pd.read_csv('./data.csv')
df.corr()
print(df)