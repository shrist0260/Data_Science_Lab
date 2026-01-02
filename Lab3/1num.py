# 1. Basic File Read & Write
# ● Create a text file and write multiple lines into it
# ● Read the contents of the file and display them on the screen
# ● Handle the case where the file does not exist using try-except

try:
    file = open("one.txt","w")
    file.write("Hello\n")
    file.write("Welcome to this place\n")
    file.write("See the day, how will turnout")
    file.close()

    file=open("one.txt","r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File not found")








