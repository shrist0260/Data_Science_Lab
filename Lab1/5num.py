# 5 Define a function that takes two numbers as arguments, and returns their greatest
common divisor (GCD).

def GCD(a,b):
    while b!=0:
        temp = a
        a = b
        b = temp % a
    return a 

n1 = input("Frst")
n2 = input("Sec")

if n1.isdigit() and n2.isdigit():
    num1 = int(n1)
    num2 = int(n2)

    result = GCD(num1, num2)
    print(f"The GCD of {num1} and {num2} is {result}")

else:
    print("please enter valid positive integers.")