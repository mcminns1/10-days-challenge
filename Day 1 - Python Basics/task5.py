#Write a program that takes two numbers as input and prints their sum, difference, product and quotient
#sum (+)
#difference (-)
#product (*)
#quotient (/)

first = int(input("First Number: "))
second = int(input("Second number: "))

total = first + second

if (first > second):
    a = first
    b = second
else:
    a = second
    b = first

diff = a - b

pro = first * second

div = round(a / b, 2)

print(f"Sum: {total}\nDifference: {diff}\nProduct: {pro}\nQuotient: {div}")