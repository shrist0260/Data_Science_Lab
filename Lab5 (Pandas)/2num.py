#  Load a CSV file into a DataFrame.
# Display column names, data types, and basic statistics.

import pandas as pd

df=pd.read_csv("2numpy.csv")
print("The columns:")
print(df.columns)
print(df.dtypes)
print(df.describe())

