# Given a list of student names and a list of their corresponding scores, use the zip() function to pair them together 
# and then apply the reduce() function from the functools module to calculate the total sum of all scores.

from functools import reduce
# reduce() is used to combine all elements of a sequence into a single value

# List of student names
students = ["Alice", "Bob", "David","Jack"]

# Corresponding scores
scores = [85, 90, 78, 92]

# Pair students with their scores using zip()
students_scores = list(zip(students, scores))
print("Student scores:", students_scores)

# Use reduce to calculate the total sum of scores
total_score = reduce(lambda acc, pair: acc + pair[1], students_scores, 0)

print("Total sum of scores:", total_score)




