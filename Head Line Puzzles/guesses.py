"""
Author: Luke Mains
Date: 3.July.2018
"""

# Imports
from collections import Counter

# Main:
message = input('Enter message to decode: ')
letter_freq = Counter()

while True:
    cipher_letters = ''
    guesses = ''

    letter_freq.clear()
    letter_freq.update([x for x in message if x.isupper()])

    print(message, '({})'.format(letter_freq.most_common(3)))

    letters = (input('Enter cipher letter and letter to swap with. \"a b\" will swap a out with b.\n').split(' '))
    cipher_letters = cipher_letters.join(letters[0].upper())
    guesses = guesses.join(letters[1].lower())

    translation_table = str.maketrans(cipher_letters, guesses)

    message = message.translate(translation_table)
