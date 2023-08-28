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

import random

choices_list = [rock, paper, scissors]

pc_choice = random.choice(choices_list)
print(f"Computer chose: \n{pc_choice}")

choice = 3

while choice < 0 or choice > 2:
  choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

if choice == 0:
  choice = rock
elif choice == 1:
  choice = paper
elif choice == 2:
  choice = scissors

print(f"You chose: \n{choice}")

if choice == rock:
  if pc_choice == scissors:
    print("You win!")
  elif pc_choice == paper:
    print("You lose.")
  else:
    print("It's a draw.")
elif choice == paper:
  if pc_choice == rock:
    print("You win!")
  elif pc_choice == scissors:
    print("You lose.")
  else:
    print("It's a draw.")
elif choice == scissors:
  if pc_choice == paper:
    print("You win!")
  elif pc_choice == rock:
    print("You lose.")
  else:
    print("It's a draw.")