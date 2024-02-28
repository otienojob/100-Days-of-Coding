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

game_images=[rock,paper,scissors]
print((2**6)*'..')
print("Welcome: Ready to Play the Rock, Paper, Scissors Game!")
print(game_images)
print((2**6)*'..')
player_name=input(print("Start by Entering Your Name: "))
gamer_input=int(input(print("Game On! Pick 0 for Rock, 1 for Paper and 2 for Scissors")))
print("Invalid User Entry. Please try again")
print(f"{player_name} , you have selected {game_images[gamer_input]} , now let's see the Computer's choice")
computer_input=random.randrange(0,2)
print(f"Computer's choice {game_images[computer_input]}")