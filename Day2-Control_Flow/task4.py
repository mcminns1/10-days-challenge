#Write a program that prompts the user for a password and keeps asking until the correct password is entered

saved = "Motho1"
password = ""
while password != saved:
    password = input("Password: ")

    if password != saved:
        print("Try again")
    else:
        print("Correct!")