#Guess the number game

#import the required modules
import random

#generate random numbers with help of random module
genrandom = random.randint(1,100)

#main game loop
def playgame():
    userguess = int(input("enter your guess: "))
    usertry = int(input("How many tries do you need"))
    attempts = 0
    while attempts < usertry:
        userguess = int(input("Enter your guess: "))
        attempts += 1
        if guesscheck(userguess, genrandom):
            break

    if attempts == usertry and userguess != genrandom:
        print("Sorry, you've used all your attempts. The number was:", genrandom)


# Program logic
def guesscheck(userguess, genrandom):
    if userguess < genrandom:
        print("Too low guess")
        return False
    elif userguess > genrandom:
        print("Too high guess")
        return False
    elif userguess == genrandom:
        print("Congratulations! You've guessed the number.")
        return True

playgame()
