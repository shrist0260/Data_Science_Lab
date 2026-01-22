# information data in that studentds 
# ID(Roll no) ,Name ,Gender, Class, (all personal info)

# another table
# student roll no subject and marks

# join this two table in one 
# in 2nd table 
# 1ta students ko 1term 2nd term 3rd term ko marks aaune frst ma (as marks ko average aaune ho tesma)
# then aarko students like wise

# Total number of students 100 as random garere lineee
# fakedata vanne library dataa line re
# 8 ota subject ko marks lineee 

import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

num_students = 100
subjects = ['Nepali','Math','English','Science','History','Geography','Computer','Grammer']

# Generate student info
student_data = {
    'Roll': list(range(1, num_students+1)),
    'Name': [fake.name() for _ in range(num_students)],
    'Age': np.random.randint(15, 20, size=num_students),
    'Address': [fake.city() for _ in range(num_students)]
}

df_info = pd.DataFrame(student_data)

# Generate random marks for each subject and 3 terminals
marks_data = []
for roll in range(1, num_students+1):
    for subject in subjects:
        marks_data.append({
            'Roll': roll,
            'Subject': subject,
            'First_Terminal': np.random.randint(50, 101),
            'Second_Terminal': np.random.randint(50, 101),
            'Third_Terminal': np.random.randint(50, 101)
        })

df_marks = pd.DataFrame(marks_data)

# Calculate average marks per subject
df_marks['Average_Marks'] = df_marks[['First_Terminal','Second_Terminal','Third_Terminal']].mean(axis=1)

# Merge student info with marks
df_final = pd.merge(df_info, df_marks, on='Roll')

# Display first few rows
print(df_final.head())

# Save to CSV
df_final.to_csv("student_final_dataset.csv", index=False)

