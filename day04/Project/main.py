rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

import random

list_of_choice = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

your_choice = list_of_choice[choice]
print("\nYour choice: " + your_choice)

random_choice = random.randint(0, 2)
computer_choice = list_of_choice[random_choice]

print("\ncomputer chooses: " + computer_choice)

list_of_current_situation = [your_choice, computer_choice]

list_of_situations = [[rock, paper], [paper, scissors], [scissors, rock], [paper, rock], [scissors, paper],
                      [rock, scissors]]

winning_statement = "YOU WIN 🏆🏆🏆"
loosing_statement = "YOU LOOSE 😭😭😭"

if choice == random_choice:
    print("it's a draw📍📍📍")
elif list_of_current_situation == list_of_situations[0]:
    print(loosing_statement)
elif list_of_current_situation == list_of_situations[1]:
    print(loosing_statement)
elif list_of_current_situation == list_of_situations[2]:
    print(loosing_statement)
elif list_of_current_situation == list_of_situations[3]:
    print(winning_statement)
elif list_of_current_situation == list_of_situations[4]:
    print(winning_statement)
elif list_of_current_situation == list_of_situations[5]:
    print(winning_statement)
