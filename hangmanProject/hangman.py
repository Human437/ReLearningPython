import random
# Line below says from the file wordsForHangman import the variable words
from wordsForHangman import words
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses a word from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    # getting user input
    # keep looping till the user guesses the word
    lives = 10
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # " ".join(['a','b','c','d']) --> 'a b c d'
        print("You have ", lives, " lives. You have guessed the following letters already: ",
              " ".join(used_letters))

        # what current word is
        word_list = [
            letter if letter in used_letters else '-' for letter in word]  # list compression
        print('Current word:', " ".join(word_list))
        user_letter = input("Guess a letter: ").upper()
        # Checks to see if the user input is in the alphabet array minus the letters in the array containing the already guessed letters
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("Letter is not in word")
        elif user_letter in used_letters:
            print("You have already guessed that letter")
        else:
            print("Invalid character")
    if lives == 0:
        print("You ran out of lives. You die. The word was ", word)
    else:
        print(f"Yay you guessed the word: {word}")


def main():
    hangman()


if __name__ == "__main__":
    main()
