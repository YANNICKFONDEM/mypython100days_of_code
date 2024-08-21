import random
rock = '''
    _____
---'   __)
        
'''

paper = '''
    _____
---'   __)___
        ___)

'''
scissors = '''
    ____________
---'   _________)
        ___)

'''

game_images = [rock, paper, scissors]

user_choice = int(input("what do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("you typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("computer chose:")
    print(game_images[computer_choice])
        
    if user_choice == 0 and computer_choice == 2:
        print("you win!")
    elif computer_choice ==0 and user_choice == 2:
        print("you lose")
    elif computer_choice > user_choice:
        print("you lose")
    elif user_choice > computer_choice:
        print("you win")
    elif user_choice == computer_choice:
        print("It's a draw")