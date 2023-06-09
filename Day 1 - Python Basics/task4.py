#Write a program that checks if a number entered by the user is even or odd

usr = int(input("Pick a number: "))

num = usr % 2

if (num == 0):
    print("Even")

else:
    print("Odd")