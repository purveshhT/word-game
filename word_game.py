import random

word_bank = ['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi']
word = random.choice(word_bank)

guessed_word = ['_'] * len(word)
attempts = 10

print("Word selected successfully!")
print("Current word:", ' '.join(guessed_word))
print("Attempts left:", attempts)