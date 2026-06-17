import random
 
# A small predefined list of words for the game
WORD_LIST = ["python", "hangman", "internship", "developer", "keyboard"]
 
MAX_ATTEMPTS = 6
 
 
def choose_word():
    """Randomly select a word from the predefined list."""
    return random.choice(WORD_LIST)
 
 
def display_progress(word, guessed_letters):
    """Show the word with guessed letters revealed and others as underscores."""
    display = [letter if letter in guessed_letters else "_" for letter in word]
    print(" ".join(display))
 
 
def play_hangman():
    word = choose_word()
    guessed_letters = set()
    wrong_attempts = 0
 
    print("=" * 40)
    print("Welcome to Hangman!")
    print(f"You have {MAX_ATTEMPTS} incorrect guesses allowed.")
    print("=" * 40)
 
    while wrong_attempts < MAX_ATTEMPTS:
        display_progress(word, guessed_letters)
        print(f"Wrong attempts: {wrong_attempts}/{MAX_ATTEMPTS}")
 
        guess = input("Guess a letter: ").lower().strip()
 
        # Basic input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue
 
        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue
 
        guessed_letters.add(guess)
 
        if guess in word:
            print("Correct guess!\n")
            # Check if the player has won
            if all(letter in guessed_letters for letter in word):
                print(f"🎉 Congratulations! You guessed the word: '{word}'")
                return
        else:
            wrong_attempts += 1
            print(f"Wrong guess! ({wrong_attempts}/{MAX_ATTEMPTS})\n")
 
    print(f"💀 Game over! You ran out of attempts. The word was: '{word}'")
 
 
if __name__ == "__main__":
    play_hangman()