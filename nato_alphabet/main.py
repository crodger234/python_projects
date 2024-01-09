


import pandas as pd

nato_dictionary = pd.read_csv("nato_phonetic_alphabet.csv")

letter_code_dict = {row.letter: row.code for index, row in nato_dictionary.iterrows()}

word_to_decode = input("Enter a word to decode: ").upper()  # Convert to uppercase for consistency

decoded_words = []
for letter in word_to_decode:
    if letter in letter_code_dict:
        decoded_words.append(letter_code_dict[letter])
    else:
        decoded_words.append(letter)

print(decoded_words)        

for letter in word_to_decode:
    if letter in letter_code_dict:
        code = letter_code_dict[letter]
        print(f"{letter}: {code}")
    else:
        print(f"{letter}: {letter}")
        



