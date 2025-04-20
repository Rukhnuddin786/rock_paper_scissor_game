import random

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
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Wellcome to rock paper scissor game......!")
print("choose 0 for rock,1 for paper, 2 for scissor")
print("This game is between user and computer....!")
game = [rock, paper, scissor]
user = int(input("enter your choice: "))
print("you have choosen:")
print(game[user])
if user >= 3 and user <= 0:
  print("Enter the valid choice....your choice is wrong")
else:

  computer = random.randint(0, 2)
  print("computer has choosen:")
  print(game[computer])
  if user == 0 and computer == 2:
    print("you have won the game....congratulations")
  elif user == 2 and computer == 0:
    print("Sorry you have lost the game....")
  elif user == computer:
    print("its a draw...")
  elif user > computer:
    print("You have won the game....congrats")
  elif user < computer:
    print("you have lost the game.....better luck next time....")
