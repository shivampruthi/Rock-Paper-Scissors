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

#Write your code below this line 👇

game_list= [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

if(user_choice >= 3):
  print("You lose")
  print("Please provide the correct input value")

else:
    

  print(game_list[user_choice])
  print("Computer chose:")
  print(game_list[computer_choice])
  
  
  
  if(computer_choice == 0 and user_choice == 1):
    print("You won")
  
  if(computer_choice == 1 and user_choice == 0):
    print("You lose")
  
  if(computer_choice == 0 and user_choice == 2):
    print("You lose")
  
  if(computer_choice == 2 and user_choice == 0):
    print("You won")
  
  if(computer_choice == 1 and user_choice == 2):
    print("You won")
  
  if(computer_choice == 2 and user_choice == 1):
    print("You lose")
  
  if(computer_choice == user_choice):
    print("Its a draw")
  
