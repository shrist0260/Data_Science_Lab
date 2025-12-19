# Store student names as keys and marks (list of integers) as values in a dictionary. Compute
# each student’s average and grade (A/B/C/D). Print the top 2 students based on average marks.

# Function to calculate grade based on average
# def get_grade(avg):
#     if avg >= 90:
#         return "A"
#     elif avg >= 75:
#         return "B"
#     elif avg >= 60:
#         return "C"
#     else:
#         return "D"


# # Dictionary to store students and their marks
# students = {}

# # Input format: Ram-80-85-90,Sita-95-92-94,Hari-70-65-75
# user_input = input("Enter students and marks (comma-separated, e.g., Ram-80-85-90,Sita-95-92-94): ")

# entries = user_input.split(",")  # split students

# for entry in entries:
#     parts = entry.split("-")
#     if len(parts) < 2:
#         print(f"Ignored invalid entry: {entry}")
#         continue

#     name = parts[0]
#     marks = []

#     for m in parts[1:]:
#         if m.isdigit():
#             marks.append(int(m))
#         else:
#             print(f"Ignored invalid mark: {m} for student {name}")

#     if marks:
#         students[name] = marks
#     else:
#         print(f"No valid marks for student {name}!")

# # ---- Processing ----
# results = []

# for name, marks in students.i





students = {}
n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = []

    m = int(input("How many subjects? "))
    for j in range(m):
        mark = int(input("Enter mark: "))
        marks.append(mark)

    students[name] = marks

averages = {}

for name, marks in students.items():
    total = 0
    for x in marks:
        total = total + x

    avg = total / len(marks)
    averages[name] = avg

    if avg >= 80:
        grade = "A"
    elif avg >= 60:
        grade = "B"
    elif avg >= 40:
        grade = "C"
    else:
        grade = "D"

    print("\n", name)
    print("Marks:", marks)
    print("Average:", avg)
    print("Grade:", grade)

first = ""
second = ""
first_avg = 0
second_avg = 0

for name, avg in averages.items():
    if avg > first_avg:
        second_avg = first_avg
        second = first
        first_avg = avg
        first = name
    elif avg > second_avg:
        second_avg = avg
        second = name

print("\nTop 2 Students:")
print("1.", first, "-", first_avg)
print("2.", second, "-", second_avg)