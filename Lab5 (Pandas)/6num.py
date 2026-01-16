#  Identify outliers in the Marks column using the IQR method.
# Remove the outliers from the dataset.

import pandas as pd

df= pd.read_csv("2numpy.csv")
Q1=df["Marks"].quantile(0.25)
Q3=df["Marks"].quantile(0.75)

IQR = Q3-Q1
print("Q1:",Q1)
print("Q3:",Q3)
print("IQR",IQR)

lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

outliers_remove=df[(df["Marks"]>lower_bound)&(df["Marks"]<upper_bound)]
print("Data After removing outliers")
print(outliers_remove)













