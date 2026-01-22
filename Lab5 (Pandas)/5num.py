# Detect duplicate rows in the dataset.
# Remove duplicates and verify the result.

import pandas as pd

df=pd.read_csv("4numpy.csv")
# print(df)

print("Detecting the duplicate value")
print(df.duplicated(subset=['Name','Age','Marks']))

print("Removing the duplicate value")
# print(df.drop_duplicates(subset=['Name','Age','Marks'], inplace=True))
# print(df)

dfs= df.drop_duplicates(subset=['Name','Age','Marks'], inplace=True)
print(dfs)
print(df)
