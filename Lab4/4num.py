# Write a Python script that takes a list of six student names and uses the random.sample() function to randomly 
# select exactly three "Volunteers" for a presentation, ensuring that no student is picked more than once in the selection.

import random 

students=["A","B","C","D","E","F"]

select = random.sample(students,3)

print("Randomly selected students", select)
# for students in select:
#     print(students)


