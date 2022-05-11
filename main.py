import pandas
data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
letter_codes = {row.letter:row.code for (index, row) in data_frame.iterrows()}
word = input("Enter a word: ").upper()
output_list = [letter_codes[letter] for letter in word]
print(output_list)

