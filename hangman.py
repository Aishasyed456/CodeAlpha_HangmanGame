import random

# List of words
words = ["book", "chair", "school", "garden", "laptop"]

# Select a random word
word = random.choice(words)

guessed = ""
chances = 6

print("===== Hangman Game =====")

while chances > 0:

    display = ""

    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"

    print("Word:", display)

    if display == word:
        print("Congratulations! You Win.")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed:
        print("You already guessed this letter.")
    elif guess in word:
        guessed += guess
        print("Correct!")
    else:
        guessed += guess
        chances -= 1
        print("Wrong!")
        print("Chances Left:", chances)

if chances == 0:
    print("Game Over!")
    print("The correct word was:", word)