Hangman Game (Python)

This is a simple, command-line interface (CLI) version of the classic Hangman Game written in Python. The program randomly selects a word from a predefined list, and the player must guess it one letter at a time before running out of attempts.

🎮 Features

Random Word Selection: Automatically picks a word from a built-in library.

Input Validation: Ensures the player only enters single alphabetic characters.

Progress Tracking: Displays the current state of the word with underscores for hidden letters.

Duplicate Detection: Alerts the player if they guess the same letter more than once.

🛠️ How to Play

Run the script: Execute the Python file in your terminal or IDE.

Guess Letters: Type a single letter and press Enter.

Correct Guesses: If the letter is in the word, it will be revealed in its correct position(s).

Incorrect Guesses: If the letter is wrong, your remaining "Wrong guesses" count will decrease.

Winning/Losing: * Win: Fill in all the blanks before reaching 6 wrong guesses.

Lose: The game ends if you reach the maximum of 6 incorrect attempts.

📋 Requirements

Python 3.x

🚀 Running the Game

To start the game, navigate to the directory containing the file and run:

Bash

python CodeAlpha_HangmanGame.py

📝 Code Overview

words: A list containing "python", "hangman", "coding", "developer", and "program".

max_wrong: Set to 6 attempts.

display: A dynamic list that tracks correctly guessed letters and underscores.
