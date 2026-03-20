import random

word_bank = ['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi']
word = random.choice(word_bank)

guessed_word = ['_'] * len(word)
attempts = 10

while attempts > 0:
    print("\nCurrent word:", ' '.join(guessed_word))
    print("Attempts left:", attempts)

    guess = input("Guess a letter: ").lower()

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
    print("\nYou've run out of attempts! The word was:", word)