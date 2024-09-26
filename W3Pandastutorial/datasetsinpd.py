import pandas as pd

# How to create dataset and dataframe based on the dataset
dataset = {
    'cars':["BMW","VOLVO","FORD"],
    'passings':[3,7,2]
}
df = pd.DataFrame(dataset)
print(df)
print(pd.__version__)