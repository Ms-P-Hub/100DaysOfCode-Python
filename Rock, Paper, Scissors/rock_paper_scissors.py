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
options = [rock,paper,scissors]

try:
    option = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

    comp_option = random.randint(0,2)

    print(options[option])

    print("Computer chose:\n")

    print(options[comp_option])


    if option == comp_option:
        print("Draw!")
    elif option == 0 and comp_option == 2:
        print("You Win!")
    elif option == 1 and comp_option == 0:
        print("You Win!")
    elif option == 2 and comp_option == 1:
        print("You Win!")
    else:
        print("You Lose!")   
except IndexError:
    print("You Typed an invalid number, You Lose!")
