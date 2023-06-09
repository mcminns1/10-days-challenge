#Write a program that checks if a number entered by the user is positive, negative, or zero

number = int(input("Choose a number: "))

if (number > 0):
    print("Positive")
elif (number < 0):
    print("Negative")
else:
    print("Zero")
