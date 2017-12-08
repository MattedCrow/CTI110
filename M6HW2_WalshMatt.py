# CTI 110
# M6HW2 - Random Number Guessing Game
# Matthew 'Melissa' Walsh
# 11.16.17
# This program prompts the user to guess a random number

from random import randint

def play_game():
    numOfGuesses = 0
    guessNum = -2
    genNum = randint(0,100)
    guessNum = int(input ("Guess a number between 0 and 100 (enter -1 to quit): "))
    numOfGuesses = numOfGuesses + 1

    while guessNum != genNum and guessNum != -1:
        if guessNum > genNum:
            print("Too high, try again.")
            guessNum = int(input ("Guess a number between 0 and 100 (enter -1 to quit): "))
            numOfGuesses = numOfGuesses + 1
        elif guessNum < genNum:
            print("Too low, try again.")
            guessNum = int(input ("Guess a number between 0 and 100 (enter -1 to quit): "))
            numOfGuesses = numOfGuesses + 1

    if guessNum == genNum:
        print("\tYou got it! It took you", numOfGuesses, "guesses.")
        

def main():
    restart = "y"

    while restart == "y":
        play_game()
        restart = input("Would you like to play again? (y/n): ")

    print("\tThanks for playing!")

# Run Main
main()
