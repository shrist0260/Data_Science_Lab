# Import pandas and create a DataFrame with columns: Name, Age, Marks.
# Display the first 5 rows and dataset shape.

import pandas as pd

students= {
    "Name":["Ram","Shyam","Hari","Sita","Gita","Rita"],
    "Age":[21,24,22,26,19,20],
    "Marks":[85,79,88,95,57,74]
}
df=pd.DataFrame(students)
print(df.head(5))
print(df.shape)