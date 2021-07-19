
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


print("Hello! Welcome to LBI rock, paper , scissors game")
user_choice=int(input("Select either 0 for rock, 1 for paper, or 2 scissors\n"))
game=([rock, paper, scissors])

if user_choice>= 3 or user_choice<=0:
  print ("Invalid number, you lose!")
else:
  print (game[user_choice])

computer_choice= random.randint(0,2)
print("Computer chose:\n")
print (game[computer_choice])


if user_choice==computer_choice:
  print("it is a draw!")
elif computer_choice==0 and user_choice== 1:
  print("You won!")
elif computer_choice==1 and user_choice==0:
  print("You lose!")
elif computer_choice==2 and user_choice==1:
    print("You lose!")
elif computer_choice==1 and user_choice==2:
    print("You won!")
elif computer_choice==2 and user_choice==0:
    print("You won!")
elif computer_choice==0 and user_choice==2:
    print("You lose!")





