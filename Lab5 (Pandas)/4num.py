# Check for missing values in the dataset.
# Fill missing numerical values with the mean

import pandas as pd

df=pd.read_csv("4numpy.csv")

# print(df)
print("Checking the null value")
print(df.isnull())
print("Replacing the null with the mean")
df.fillna(df.mean(numeric_only=True),inplace=True)
print(df)



