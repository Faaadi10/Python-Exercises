import random

# generating a number between 1 and 20
number = random.randint(1,20)

# Setting conditions
attempts = 0
max_attempts = 5

print("Guess the number game")
print("Guess the number I've generated. You've got 5 attempts.\n")

# Checking if correct or not
while (attempts < max_attempts):
    guess = int(input("guess the number I've generated\n"))
    if (guess == number):
        print("Congrats, you won.")
        break
    elif (guess > number):
        print("Lower than that. Try Again !")
    elif (guess < number):
        print("Higher than that. Try again!")
    elif (number > 20):
        print("Choose between 1 to 20")

    attempts = attempts + 1

if (attempts == max_attempts):
    print("You've finished your attempts")
