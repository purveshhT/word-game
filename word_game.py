import random

word_bank = ['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi']

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

while True:
    word = random.choice(word_bank)
    guessed_word = ['_'] * len(word)
    attempts = 6
    guessed_letters = []

    print("\n🎮 New Game Started!")

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
            print("\n🎉 Congratulations!! You guessed the word:", word)
            break

    if attempts == 0 and '_' in guessed_word:
        print(hangman_stages[6])
        print("\n💀 Game Over! The word was:", word)

    # 🔁 Play again option
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing! 👋")
        break