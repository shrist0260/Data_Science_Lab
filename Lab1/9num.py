# 9. Write a program that takes a temperature in Celsius, and converts it to Fahrenheit and Kelvin, based on the choice of user.

temp = input("Enter Temperature")

if temp.isdigit():
    celsius = float(temp)

    print("Choose conversion type")
    print("1. Fahreneit")
    print("2.Kelvin")
    choice = input("Enter 1 or 2 \n")

    if choice == "1":
        fahreneit = (celsius * 9/5) +32
        print(f"{celsius} is equal to {fahreneit} F")
    elif choice == "2":
        Kelvin = celsius + 273.15
        print(f"{celsius} is equal to {Kelvin} k.")  
    else:
        print("Invalid choice")

else:
    print("Enter a valid number")