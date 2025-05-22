import random

def hangman():
    words = ["python", "developer", "hangman", "programming"]
    word = random.choice(words)
    guessed = ['_'] * len(word)
    tries = 6
    guessed_letters = []

    print("Welcome to Hangman!")

    while tries > 0 and '_' in guessed:
        print(f"Word: {' '.join(guessed)}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("Already guessed.")
            continue
        guessed_letters.append(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
        else:
            tries -= 1
            print(f"Wrong! {tries} tries left.")

    if '_' not in guessed:
        print(f"You won! The word was: {word}")
    else:
        print(f"You lost! The word was: {word}")

if __name__ == "__main__":
    hangman()
