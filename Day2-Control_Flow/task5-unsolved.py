#Write a program that prints the Fibonacci sequence up to a given number using a for loop.

x = int(input("Choose a number: "))
y = 0

for i in range(0, x):
    y += 1
    i = i + y
    print (i)