import random

# Get the words
with open("Day 7 - Hangman\words", "r") as file:
    words = file.readlines()
# Make sure its clean
words = [word.lower().strip("\n") for word in words]
# Pick random word
rand_word = random.choice(words)

print(rand_word)

underscores = list("_"*len(rand_word))

print(underscores)


guess = " "
counter = 0
while True:
    user_guess = input("Guess a letter: ")
    if user_guess in rand_word:
        for i, letter in enumerate(rand_word):
            if letter == user_guess:
                underscores[i] = letter
                continue

    else:
        print("no")
        break

print(underscores)
