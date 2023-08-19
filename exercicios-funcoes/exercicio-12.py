import random
from random import randrange

def main():
    word = input("informe uma palavra para ser embaralhada: ")
    print("a palavra embaralhada é: " + shuffle_string(word.lower()))


def shuffle_string(word):
    new_word = ""
    letters = list(word)
    word_length = len(word)
    for i in range(word_length):
        letter_index = random.randrange(len(letters))
        new_word += letters[letter_index]
        letters.pop(letter_index)

    return new_word


main()