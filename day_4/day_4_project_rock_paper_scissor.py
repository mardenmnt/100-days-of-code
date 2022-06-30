
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

game_images = [rock, paper, scissors]

player_choice = int(input("\nWhat do you choose?\n0 - Rock\n1 - Paper\n2 - Scissors.\n"))

if player_choice > 2 or player_choice < 0:
    print("\nYou typed an invalid number, you lose!")

else:
    print(f"{game_images[player_choice]}")

    computer_choice = random.randint(0, 2)
    
    print('\nThe computer chose...')
    print(game_images[computer_choice])


    if player_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and player_choice == 2:
        print("You lose")
    elif computer_choice > player_choice:
        print("You lose")
    elif player_choice > computer_choice:
        print("You win!")
    elif computer_choice == player_choice:
        print("It's a draw")



    ## OR ##



    # if player_choice == 0:
    #     if computer_choice == rock:
    #         print(f"{rock}\nDraw")
    #     elif computer_choice == paper:
    #         print(f"{paper}\nYou Lose") 
    #     elif computer_choice == scissors:
    #         print(f"{scissors}\nYou Won!!")

    # elif player_choice == 1:
    #     if computer_choice == rock:
    #         print(f"{rock}\nYou Won!!")
    #     elif computer_choice == paper:
    #         print(f"{paper}\nDraw")
    #     elif computer_choice == scissors:
    #         print(f"{scissors}\nYou Lose")

    # elif player_choice == 2:

    #     if computer_choice == rock:
    #         print(f"{rock}\nYou Lose")
    #     elif computer_choice == paper:
    #         print(f"{paper}\nYou Won!!")
    #     elif computer_choice == scissors:
    #         print(f"{scissors}\nDraw")
