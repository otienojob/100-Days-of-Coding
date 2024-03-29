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
player_name=input(print("Start by Entering Your Name: \n"))

#error exception
gamer_input=-1
while gamer_input<0 or gamer_input>2:
    try:
        gamer_input=int(input(print("Game On! Pick 0 for Rock, 1 for Paper and 2 for Scissors")))
        if gamer_input <0 or gamer_input>2:
            print("Invalid entry. Kindly enter 0, 1 or 2")
    except ValueError:
        print("Invalid entry. Try again")
#end of exception block

print(f"{player_name} , you have selected {game_images[gamer_input]} , now let's see the Computer's choice")

#generate computer selection

computer_input=random.randrange(0,2)
print(f"Computer's choice is  {game_images[computer_input]}")

#getting to know the winner

if gamer_input==0 and computer_input==2:
    print(f'{player_name}, You Win!')
elif gamer_input==2 and computer_input==0:
    print(f'{player_name}, You Lose!')
elif gamer_input<computer_input:
    print(f'{player_name}, You Lose!')
elif gamer_input<computer_input:
    print(f'{player_name}, You Win!')
elif gamer_input==computer_input:
    print(f'{player_name}, You Draw!')