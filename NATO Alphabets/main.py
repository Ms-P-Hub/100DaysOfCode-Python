import pandas

def nato_alphabet():
    name = input("Enter Name: ").upper()       

    data = pandas.read_csv("./NATO Alphabets/nato_phonetic_alphabet.csv")

    try:
        format_dict = {row['letter']:row['code'] for indGex, row in data.iterrows()}
        nato = [format_dict[i] for i in name]
        return print(nato)
    except KeyError(""):
        nato_alphabet()

nato_alphabet()