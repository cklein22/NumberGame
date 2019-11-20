"""
This program is a guessing game between the computer and the user.
The computer will generate a random number between 1 and 10 and the user will try and guess that number.
After 3 attempts, the program will reveal the correct answer if it has not been guessed.
The program will then ask if the user would like to play again.

Created by Cecelia Klein
October 8, 2019
"""

print "Welcome to the number guessing game!"
name = raw_input ("What is your name? ")

import random
guesses = 0
number = random.randint(1, 10)

print('Hello, ' + name + '! I am thinking of a number between 1 and 10.')

#the player will have three tries to guess the number.
while guesses < 3:

  guess = raw_input('Guess the number:  ')
  guess = int(guess)

  if guess > 0 and guess < 10:

    guesses = guesses + 1

    if guess < number:
      print('Incorrect! Guess a higher number.')
    if guess > number:
      print('Incorrect! Guess a lower number.')
    if guess == number:
      break
  else:
    print ("Sorry, try entering a number between 1 and 10")

#if the player guesses correctly, the program will congratulate them and reveal how many guesses it took.
if guess == number:
    guesses = str(guesses)
    print('Great work, ' + name + '! It took you ' + guesses + ' to guess the number correctly!')

#if the player does not guess the number after three tries, the correct answer is revealed.
if guess != number:
    number = str(number)
    print('I was thinking of ' + number)
    print('Would you like to try one more time?')

#the player will then have the option to repeat the game once more.
tryagain = raw_input ("Enter Y to try again, enter N to close the program: ")

if tryagain == "Y" or tryagain == "y":
    import random
    guesses = 0
    number = random.randint(1, 10)
    print('Lets see if you can guess the number this time, ' + name + '! I am thinking of a number between 1 and 10')

    while guesses < 3:
        print('Guess the number.')
        guess = input()
        guess = int(guess)

        guesses = guesses + 1

        if guess < number:
            print('Incorrect! Guess a higher number.')
        if guess > number:
            print('Incorrect! Guess a lower number.')
        if guess == number:
            break

    if guess == number:
        guesses = str(guesses)
        print('Great work, ' + name + '! It took you ' + guesses + ' to guess the number correctly!')
        print('Thanks for playing!')

    if guess != number:
        number = str(number)
        print('Incorrect... I was thinking of ' + number)
        print('Thanks for playing!')

#if the player enters N, meaning they do not want to play again, or the player does not enter Y or N, the program will close.
elif tryagain == "N" or tryagain == "n":
        print('Thanks for playing!')

else:
    print "Error! Next time, please enter either Y or N."

print "Exiting Program..."
