# Create a new column by transforming Marks (e.g., Marks / 10).
# Rename columns and save the cleaned dataset to a CSV file.

import pandas as pd

df=pd.read_csv("2numpy.csv")
df["Marks_transform"]= df["Marks"]/10
print(df)

df.to_csv("Cleaned_2numpy.csv",index=False)

print("Cleaned data save successfully to csv file")



