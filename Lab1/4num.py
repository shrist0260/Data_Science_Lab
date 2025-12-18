# 4 Write a python program that prints the Fibonacci series up to n terms.
n=input("Enter a number")
if n.isdigit():
    num= int(n)
    a=0
    b=1

    # print(f"fibonaaci series upto to {num} term:")
    for i in range(num):
        print(a)
        temp= a
        a=b
        b= temp+a

else:
    print("enter valid integer")