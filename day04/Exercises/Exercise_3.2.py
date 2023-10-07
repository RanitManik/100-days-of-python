import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

random_number = random.randint(0, (len(names) - 1))
who_is_paying = names[random_number]
print(who_is_paying + " is going to buy the meal today!")
