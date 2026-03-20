import random

word_bank = ['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi']
word = random.choice(word_bank)

guessed_word = ['_'] * len(word)
attempts = 6
guessed_letters = []

hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    """
]

while attempts > 0:
    wrong_guesses = 6 - attempts
    print(hangman_stages[wrong_guesses])
    print("Current word:", ' '.join(guessed_word))
    print("Attempts left:", attempts)
    print("Guessed letters:", ' '.join(guessed_letters))

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("Great guess!")
    else:
        attempts -= 1
        print("Wrong guess!")

    if '_' not in guessed_word:
        print("\nCongratulations!! You guessed the word:", word)
        break

if attempts == 0 and '_' in guessed_word:
    print(hangman_stages[6])
    print("\nYou've run out of attempts! The word was:", word)