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

lives = 5 
letters_guessed = []

while True:
    
    print(underscores)
    user_guess = input("Guess a letter: ").lower()
    letters_guessed.append(user_guess)
    print(f"You have guessed these letters: {letters_guessed}")
    
    if user_guess in rand_word:
        for i, letter in enumerate(rand_word):
            if letter == user_guess:
                underscores[i] = letter
                
        if "_" not in underscores:
            print("You win!")
            print(f"You had {lives} lives left")
            break 
        else:
            print(underscores)
            continue

    else:
        lives -= 1
        print(f"That letter is not in the word. You have lost 1 life.\nYou have {lives} lives left")
        if lives == 0:
            print(f"You're out of lives! You lose. The word was {rand_word}")
            break
        continue