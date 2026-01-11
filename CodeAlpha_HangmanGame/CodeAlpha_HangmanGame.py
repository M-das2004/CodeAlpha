import random

# Predefined list of words
words = ["python", "hangman", "coding", "developer", "program"]

# Randomly select a word
word = random.choice(words)

# Game variables
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

# Create display word with underscores
display = ["_"] * len(word)

print("Welcome to Hangman Game!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses.\n")

# Game loop
while wrong_guesses < max_wrong and "_" in display:
    print("Word:", " ".join(display))
    print(f"Wrong guesses left: {max_wrong - wrong_guesses}")
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("Good guess!\n")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        wrong_guesses += 1
        print("Wrong guess!\n")

# Final result
if "_" not in display:
    print("Congratulations! You guessed the word:", word)
else:
    print("Game Over! The word was:", word)

