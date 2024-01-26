# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
option = int(
    input(
        " Enter '0' if you want a non-order-randomised password or, \n '1' if you want an order-randomised password: "))
if option == 0 or option == 1:
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

first_password = ""
second_password = ""
password_list = []

if option == 0:
    # Eazy Level - Order not randomised:
    # e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    # Generating random letters
    for i in range(0, nr_letters):
        first_password += random.choice(letters)

    # Generating random symbols
    for i in range(0, nr_symbols):
        first_password += random.choice(symbols)

    # Generating random numbers
    for i in range(0, nr_numbers):
        first_password += random.choice(numbers)

    print(f"\nYour not orderly randomized password is \n  {first_password} \n")

elif option == 1:
    # Hard Level - Order of characters randomised:
    # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

    # Generating random letters
    for i in range(0, nr_letters):
        password_list.append(random.choice(letters))

    # Generating random symbols
    for i in range(0, nr_symbols):
        password_list += random.choice(symbols)

    # Generating random numbers
    for i in range(0, nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)
    second_password = ''.join(password_list)

    print(f"Your orderly randomized password is \n  {second_password} \n")
else:
    print("Plz Enter a valid option...")
