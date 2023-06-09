#Write a program that takes a temperature in Celsius and converts it to Fahrenheit

c = float(input("What is your temperature (in celsius): "))

f = (c * 1.8) + 32
ans = round(f, 2)

print(f"Your temperature in Fahrenheit if {ans} F")