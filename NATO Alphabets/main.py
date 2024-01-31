import pandas

name = input("Enter Name: ").upper()

data = pandas.read_csv("./NATO Alphabets/nato_phonetic_alphabet.csv")

format_dict = {row['letter']:row['code'] for indGex, row in data.iterrows()}

nato = [format_dict[i] for i in name]
print(nato)