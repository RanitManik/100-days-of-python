# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

years = 90 - int(age)
months = years * 12
weeks = years * 52
days = 365 * years
print(f"You have {days} days, {weeks} weeks, and {months} months left.")
