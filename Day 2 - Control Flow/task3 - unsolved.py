#Write a a program that calculates the factorial of a number using a while loop
#number x (number-1)
num = int(input("Choose a number: "))

i = num

while num > 0:
    a = i * num
    num -= 1
    print(a)