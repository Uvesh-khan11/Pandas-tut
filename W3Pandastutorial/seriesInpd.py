import pandas as pd
# A Pandas Series is like a column in a table.
# It is a one-dimensional array holding data of any type.

# a = [1,7,2]
# b = [2,4,3]
# df = pd.Series(a) # Create a Series
# df = pd.Series(b) # if we do like this it will take the latest one
# print(df[0]) # you can print values like this as general
# df = pd.Series(a, index = ["X", "Y", "Z"]) # Change your own labels / after doing this it come xyz not 012
# print(df["X"])


# Now Create a key value object as series
# calories = {"Day1":420,"Day2":380,"Day3":390}
# df = pd.Series(calories)
# # print(df) # And you can get any value just like above we get

# # Create a Series using only data from "day1" and "day2": This al tricks good with large datasets
# calories = {"Day1":420,"Day2":380,"Day3":390}
# df1 = pd.Series(calories, index = ["Day1", "Day2"])
# print(df1)


# Create a DataFrame from two Series:

# data = {
#     "calories" :[420,390,230],
#     "duration":[50,40,45]
# }
# df = pd.DataFrame(data, index = ["A","B","C"]) # You Change index also
# print(df)
