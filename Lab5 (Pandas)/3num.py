# Select rows where Marks > 60.
# Select only Name and Marks columns.

import pandas as pd

df=pd.read_csv("2numpy.csv")

results= df[df["Marks"]>60][["Name","Marks"]]
print(results)

