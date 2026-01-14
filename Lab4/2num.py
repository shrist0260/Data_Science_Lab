# Use a list comprehension to create a new list containing only the even numbers between
# 1 and 20, demonstrating a more concise and readable alternative to traditional loops.


# Create a list of even numbers between 1 and 20

# frst i = expression   and in for i is items in range from 1 to 21
even_numbers = [i for i in range(1, 21) if i % 2 == 0]

# Display result
print("Even numbers between 1 and 20:", even_numbers)




