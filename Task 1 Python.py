import random

def choose_word():
    # List of words to choose from
    words = ['python', 'hangman', 'programming', 'developer', 'challenge', 'computer', 'algorithm']
    return random.choice(words)

def display_word(word, guessed_letters):
    # Display the word with guessed letters revealed and others hidden
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # You can change the number of allowed incorrect guesses

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    while incorrect_guesses < max_incorrect_guesses:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        
        guess = input("Guess a letter: ").lower()

        # Ensure the guess is a single alphabetic character
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! The letter {guess} is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Oops! The letter {guess} is not in the word.")
        
        # Check if the player has guessed the entire word
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You've guessed the word: {word}")
            break
    else:
        print(f"\nGame over! The word was: {word}")

if __name__ == "__main__":
    hangman()

