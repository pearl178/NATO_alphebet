import pandas
data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
letter_codes = {row.letter:row.code for (index, row) in data_frame.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [letter_codes[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()
