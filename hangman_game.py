import random

# List of words
words = ["australia", "pomegrant", "mobile", "construction", "umbrella"]

# Choose a random word
word = random.choice(words)
word_letters = list(word)
display_word = ["_"] * len(word)
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("Welcome to Hangman!")
print(" ".join(display_word))

# Game loop
while incorrect_guesses < max_incorrect and "_" in display_word:
    guess = input("Guess a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():  # gues.isalpha() is used to check whether the guess string is consist of letters or numbers. If it is letters than it says true if it is numbers it says false
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try a different letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_letters:
        print(f"Good job! '{guess}' is in the word.")
        # Reveal the letter in display_word
        for i, letter in enumerate(word_letters):
            if letter == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print(f"Sorry! '{guess}' is not in the word. ({incorrect_guesses}/{max_incorrect} wrong guesses)")

    print(" ".join(display_word))

# Check win or loss
if "_" not in display_word:
    print("Congratulations! You guessed the word:", word)
else:
    print("Game over! The word was:", word)
    
