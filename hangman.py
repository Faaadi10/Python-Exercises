# Introduction
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)


# Randomly chose a word between a list of words.
import random
last_names = ["Messi", "Ronaldo", "Mbappe", "Salah", "Hazard", "Lewandowski", "Modric", "Bale", "Suarez", "Kroos"]
chosen_word = random.choice(last_names)
print("Choosen word is " + chosen_word)

# Setting the total number of lives of hangman to be 6
lives = 6

# Setting the hangman in a string. Each position of the string denotes each life losing.
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Adding blanks at each letter position
display = []
length = len(chosen_word)
for char in range(length):
    display.append("_")
print(display)

end_of_game = False


while not end_of_game:

    # Asking user to guess a letter from the word
    guess = input("Guess a letter : ").lower()


    # # To check if the guess is in the word
    # for letter in chosen_word:
    #     if letter == guess:
    #         print("Right")
    #     else:
    #         print("Wrong")


    # Replacing the blanks with correct guess letter
    for position in range(length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if guess not in chosen_word:
        lives = lives - 1
        print(f"You guessed {guess}, that's not in the word, you lose a life")
        if lives == 0:
            end_of_game = True
            print("You Lost")




    # Checking won or not

    if "_" not in display:
        end_of_game = True
        print("You Win")


    print(stages[lives])
