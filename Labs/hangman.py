# Hangman game

gallows = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    '''
    ]

# make a word list for your game
# grab a random word from your list and store it as a variable
# in a loop, do the following
# display the hangman using the gallows
# display the used letters so the user knows what has been selected
    # make spaces between letters
# display the length of the word to the user using blank spaces and used letters
# prompt the user to guess a letter
# don't allow the user to select the same letter twice
# if the guess is incorrect increment incorrect_guesses by 1
# if the incorrect_guesses is greater than 8, tell the user they lost and exit the program
# if the user gets all the correct letters, tell the user they won
# ask if they want to play again

import random

# generate random word
word_list = ["coconut", "beach", "tropical", "ocean", "sunny", "relaxing", "sandy", "summer"]
# chosen_word = random.choice(word_list)
chosen_word = word_list.pop(random.randrange(len(word_list)))

# lists
guessed_letters = []
correct_letters = []
incorrect_letters = []

print("WELCOME TO SUMMER-THEMED HANGMAN!")

done = False

# game loop
while not done:

    # drawing the hangman
    print(gallows[len(incorrect_letters)])

    # blanks for letters
    blanks = "_" * len(chosen_word)
    for i in range(len(chosen_word)):
        if chosen_word[i] in correct_letters:
            blanks = blanks[:i] + chosen_word[i] + blanks[i + 1:]
    for letter in blanks:
        print(letter, end=" ")
    print()
    print()

    # guessed letter list
    print("Guessed letters: ", end="")
    for letter in guessed_letters:
        print(letter + " ", end=" ")
    print()

    # player letter guesses
    guess = (input("Guess a letter: "))

    # restrictions on guess
    if len(guess.lower()) != 1:
        print()
        print("You can only guess one letter.")
    elif guess.lower() not in "abcdefghijklmnopqrstuvwxyz":
        print()
        print("You can only guess a letter.")
    elif guess.lower() in guessed_letters:
        print()
        print("You already guessed this letter.")
    # checks if letter in word, adds to respective lists
    else:
        if guess.lower() in chosen_word:
            correct_letters.append(guess)
            guessed_letters.append(guess)

            found_all_letters = True
            for i in range(len(chosen_word)):
                if chosen_word[i] not in correct_letters:
                    found_all_letters = False
                    break
            if found_all_letters:
                print()
                print("You won! The word was:", chosen_word)
                done = True

        else:
            incorrect_letters.append(guess)
            guessed_letters.append(guess)
            # lose game
            if len(incorrect_letters) == 6:
                print(gallows[6])
                print("You hanged the man & ran out of guesses! The word was:", chosen_word)
                done = True

    if done:
        play_again = (input("Do you want to play again? Type yes or no: "))
        if play_again.lower() == "yes":
            guessed_letters = []
            correct_letters = []
            incorrect_letters = []
            chosen_word = word_list.pop(random.randrange(len(word_list)))
            done = False
        else:
            break


















