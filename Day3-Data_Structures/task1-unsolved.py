#Write a program that sorts a list of numbers in ascending order.

list_of_numbers = input("Input a list of numbers and separate them with a comma: ")
list1 = list_of_numbers.split()
list1.sort()

print(list1)