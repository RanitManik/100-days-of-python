import math


# Write your code below this line 👇


def prime_checker(number):
    for num in range(2, math.floor(number / 2 + 1)):
        if (number % num) == 0:
            print("It's not a prime number.")
            return
    print("It's a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
