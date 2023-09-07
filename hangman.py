# Randomly chose a word between a list of words.
import random
last_names = ["Messi", "Ronaldo", "Mbappe", "Salah", "Hazard", "Lewandowski", "Modric", "Bale", "Suarez", "Kroos"]
chosen_word = random.choice(last_names)
print("Choosen word is " + chosen_word)


# creating a list
display = []
word_length = len(chosen_word)
for letter in chosen_word:
    display.append("_")
print(display)


# to check if guessed letter is present in the random chosen word
# using a while loop to let the user guess again. The loop should stop only when user has guessed all the letters in the chosen word and display has noo more blanks left.

while
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

# using a while loop to let the user guess again. The loop should stop only when user has guessed all the letters in the chosen word and display has noo more blanks left.
