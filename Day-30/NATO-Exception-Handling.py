import pandas as pd


data = pd.read_csv('nato_phonetic_alphabet.csv')
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate():
    word = input('Enter a word: ').upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print('Sorry, only letters in the alphabet please')
        generate()
    else:
        print(output_list)

generate()
