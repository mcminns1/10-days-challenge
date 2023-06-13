#Write a a program that calculates the factorial of a number using a while loop
#number x (number-1)
num = int(input("Choose a number: "))

i = 1
fact = 1

if num < 0:
    print("Input is Negative")
elif num == 0:
    print("Input is Zero")
elif num > 0:
    while i <= num:
        fact *= i
        i += 1
    print(fact)
