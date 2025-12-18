# wite a program to take two number as input from the user, and  print their sum.
a= float(input("Enter frst number"))
b= float(input("Enter second number"))
c=a+b

if c.is_integer():
    print(int(c))
else:
    print(c)
