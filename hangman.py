"""A beginner-friendly console Hangman game.

Run with: python hangman.py
Only Python's standard library is required.
"""

import random

MAX_ATTEMPTS = 6
WORDS = [
    "python", "computer", "keyboard", "programming", "internet",
    "science", "student", "function", "variable", "developer",
    "project", "library", "software", "hangman", "terminal",
]

HANGMAN_STAGES = [
    r"""
     +---+
     |   |
         |
         |
         |
         |
    =========
""",
    r"""
     +---+
     |   |
     O   |
         |
         |
         |
    =========
""",
    r"""
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
""",
    r"""
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========
""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========
""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========
""",
]


def choose_word():
    """Return a randomly selected word from the built-in word list."""
    return random.choice(WORDS)


def display_game(word, guessed_letters, wrong_guesses):
    """Show the gallows, masked word, used letters, and attempts remaining."""
    masked_word = " ".join(letter if letter in guessed_letters else "_" for letter in word)
    print(HANGMAN_STAGES[wrong_guesses])
    print(f"\nWord: {masked_word}")
    print("Guessed letters:", " ".join(sorted(guessed_letters)) or "None")
    print(f"Attempts remaining: {MAX_ATTEMPTS - wrong_guesses}")


def get_guess(guessed_letters):
    """Get one valid alphabetic character; repeated guesses are not penalized."""
    while True:
        guess = input("\nGuess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha() or not guess.isascii():
            print("Please enter one English letter (A-Z).")
        elif guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
        else:
            return guess


def play_game():
    """Run one complete round of Hangman."""
    word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0

    print("\n================================")
    print("       HANGMAN WORD GAME")
    print("================================")
    print(f"Guess the hidden word in {MAX_ATTEMPTS} incorrect attempts.")

    while wrong_guesses < MAX_ATTEMPTS and not all(
        letter in guessed_letters for letter in word
    ):
        display_game(word, guessed_letters, wrong_guesses)
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! The letter '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")

    display_game(word, guessed_letters, wrong_guesses)

    if all(letter in guessed_letters for letter in word):
        print(f"\nYOU WIN! The word was '{word}'. Congratulations!")
    else:
        print(f"\nGAME OVER! The correct word was '{word}'. Better luck next time!")


def main():
    """Start the game and offer another round after each result."""
    while True:
        play_game()
        again = input("\nWould you like to play again? (y/n): ").strip().lower()
        if again not in {"y", "yes"}:
            print("\nThanks for playing Hangman. Goodbye!")
            break


if __name__ == "__main__":
    main()
