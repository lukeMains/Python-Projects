"""
Author: Luke Mains
Date: 3.July.2018
"""

cipher = input('Enter ciphertext:')
plain = input('Enter plaintext:')

# This method is from stack overflow. I'm not sure how it works.
seen = set()
seen_add = seen.add
cipher_letters = ''.join([x for x in cipher if not (x in seen or seen_add(x))])

seen.clear()
seen_add = seen.add
plain_letters = ''.join([x for x in plain if not (x in seen or seen_add(x))])
# -------------------

table = str.maketrans(cipher_letters, plain_letters)

print(cipher.translate(table))
