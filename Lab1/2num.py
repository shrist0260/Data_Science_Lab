# 2 Write a program that checks if a given string is palindrome.
a="Eye"

# print(a[-1])
# print(a[:-1])

if a == a[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")