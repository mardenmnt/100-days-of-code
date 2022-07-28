

from random import randint
from art import logo
from os import system

# global scopes(variables)
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
GAME_ON = True


def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns the number of turns remaining"""
    if guess < answer:
        print("Too low")
        return turns - 1
    elif guess > answer:
        print("Too high")
        return turns - 1
    else:
        print(f"\nYou got it! The answer was {answer}")

def set_difficulty():
    level = input("\nChoose a difficulty. Type 'easy' or 'hard' ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def choose_continue():
    while GAME_ON:
        choose_continue = input("\nCan you run again? Type 'yes' or 'no' ").lower()
        if choose_continue == "no":
            print("\nGoodbye")
            return not GAME_ON
        else:
            system("clear")
            game()


def game():
    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("\nYou've run out of guesses, you lose.")
            return  # exit the function
        elif guess != answer:
            print("\nGuess again:")
        
print(logo)

game()
choose_continue()




    ### OR ###




# from random import randint
# from os import system
# from art import logo

# def attempts_remaining(start):
#     for num in range(start, -1, -1):
#             if num == 0:
#                 print("\nYou've run out of guesses, you lose.")
#                 break

#             print(f"You have {num} attempts remaining to guess the number.")
            
#             guess = int(input("Make a guess: "))

#             if guess < number:
#                 print("Too low")
#             elif guess > number:
#                 print("Too high")
#             else:
#                 print(f"\nYou got it! The answer was {number}")
#                 break

# print(logo)
# print("\nWelcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100.")

# game_on = True

# while game_on:

#     choose_difficulty = input("\nChoose a difficulty. Type 'easy' or 'hard' ").lower()
#     number = randint(1, 100)
#     print(number)

#     if choose_difficulty == "easy":
#         attempts_remaining(10)
#     elif choose_difficulty == "hard":
#         attempts_remaining(5)
    
#     choose_continue = input("\nCan you run again? Type 'yes' or 'no' ").lower()
#     if choose_continue == "no":
#         game_on = False
#         print("\nGoodbye")
#     else:
#         system("clear")
