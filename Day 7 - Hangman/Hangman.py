import random
import ASCII_ART


print(ASCII_ART.logo)

# Choose the difficulty of word
difficulty = input(f"\nChoose the difficulty. Easy, Medium or Hard: ").lower().strip()

# Get the words based on difficulty
if difficulty == "easy":
    with open("Day 7 - Hangman\easy_words.txt", "r") as file:
        words = file.readlines()

if difficulty == "medium":
    with open("Day 7 - Hangman\medium_words.txt", "r") as file:
        words = file.readlines()

if difficulty == "hard":
    with open("Day 7 - Hangman\hard_words.txt", "r") as file:
        words = file.readlines()

# Make sure its clean
words = [word.lower().strip("\n").rstrip() for word in words]

# Pick random word
rand_word = random.choice(words)

# Show how many letters are in the word
underscores = list("_"*len(rand_word))

lives = 6 
letters_guessed = []
print(f"\n {underscores}")

print(ASCII_ART.stages[6])
while True:
    user_guess = input("Take a guess: ").lower()
    
    if user_guess in letters_guessed:
            print("You have already guessed that")
            continue

    letters_guessed.append(user_guess)
    print(f"You have guessed: {letters_guessed}")

    if user_guess in rand_word:
        for i, letter in enumerate(rand_word):
            if letter == user_guess:
                underscores[i] = letter

        if "_" not in underscores:
            print("You win!")
            print(f"You had {lives} lives left")
            print(f"The word was {rand_word}")
            break 
        
        elif user_guess == rand_word:
            print(ASCII_ART.trophy)
            break
        
        else:
            print(underscores)
            continue

    else:
        lives -= 1
        print(f"That letter is not in the word. You have lost 1 life.\n You have {lives} lives left")
        print(ASCII_ART.stages[lives])
        print(underscores)
        if lives == 0:
            print(f"You're out of lives!\nYou lose.\nThe word was {rand_word}.")
            break
        continue