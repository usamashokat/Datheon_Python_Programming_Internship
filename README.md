# Hangman Word Guessing Game (Console)

**Dathon Python Internship — Task 1**  
A beginner-friendly, interactive Hangman game built with Python.

## Features

- Randomly selects a hidden word from a built-in English word list.
- Displays the word as blanks and reveals correctly guessed letters.
- Gives the player a maximum of **6 incorrect guesses**.
- Shows ASCII gallows art as incorrect guesses are made.
- Tracks previously guessed letters.
- Does not deduct an attempt for a repeated guess.
- Validates input so the player must enter one English letter at a time.
- Displays a clear win/loss message and offers a replay option.
- Uses only Python's standard library; no extra packages are required.

## Requirements

- Python 3.8 or newer
- VS Code, PyCharm, or any terminal/command prompt

## How to Run

1. Download or clone this repository.
2. Open the project folder in VS Code or a terminal.
3. Run:

   ```bash
   python hangman.py
   ```

   On some systems, use `python3 hangman.py` instead.

## Project Structure

```text
Dathon_Python_Internship_Task1_Hangman/
├── hangman.py
└── README.md
```

## How to Play

1. The game chooses a random word.
2. Enter one English letter when prompted.
3. Correct guesses reveal the matching letters.
4. Incorrect guesses add one part to the ASCII gallows and reduce the remaining attempts.
5. Guess the full word before reaching six incorrect guesses to win.
6. Enter `y` to start another round or `n` to exit.

## Concepts Demonstrated

- Strings and string manipulation
- Lists and random selection
- Sets for tracking guessed letters
- Loops and conditional statements
- Functions and modular program structure
- Input validation

---

**Author:** Muhammad Usama Shokat  
**Internship:** Dathon Python Programming Internship
