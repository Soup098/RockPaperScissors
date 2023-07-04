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
images = [rock, paper, scissors]
user_choice = int(input('Choose an option: [0] for Rock [1] for Paper or [2] '
               'for Scissors. to exit, type exit\n'))
if user_choice > 2 or user_choice< 0:
    print('invalid choice, You Lose!')
    exit()
else:
    print('You Chose')
    print(images[user_choice])

comp_choice = random.randint(0, 2)
print('The computer chose:')
print(images[comp_choice])

if user_choice == 0 and comp_choice == 2:
    print('You Win')
elif comp_choice == 0 and user_choice == 2:
    print('You Lose')
elif user_choice > comp_choice:
    print('You Win')
elif comp_choice > user_choice:
    print('You Lose')
elif comp_choice == user_choice:
    print('Its A Tie!')
else:
    print('invalid choice, You Lose!')

