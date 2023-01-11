### Hangman Game

word_list=['ardvark','baboon','camel']

## Todo-1 : Randomly choose a word from word_list and assign it  to a variable 
# called chosen_word
import random
chosen_word = random.choice(word_list)



##Todo_02: Ask the user to guess a letter and assign their answer to a variable called
# guess . Make guess lowercase

guess = input("Guess a letter : ").lower()

## Todo_03: Check if the letter the user guessed (guess) is one of the letters in 
# the letters  in the chosen_word

for letter in word_list:
    if letter == chosen_word:
        print("Right")
    else:
        print("Wrong")    