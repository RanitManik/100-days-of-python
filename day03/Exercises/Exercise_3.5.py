# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

true_word = "true"
love_word = "love"

name1 = name1.lower()
name2 = name2.lower()

true_count = sum(name1.count(letter) + name2.count(letter) for letter in true_word)
love_count = sum(name1.count(letter) + name2.count(letter) for letter in love_word)

love_score = int(f"{true_count}{love_count}")

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
