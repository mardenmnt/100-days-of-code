#Step 1 

import random

word_list = ["aardvark", "baboon", "camel"]

# ToDo-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

sort_word = random.choice(word_list)

# ToDo-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

letter = input("Guess a letter: ").lower()

# ToDo-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for i in sort_word:
  if letter == i:
    print("Right")
  else:
    print("Wrong")
