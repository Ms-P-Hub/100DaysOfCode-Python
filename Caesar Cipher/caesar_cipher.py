from art import logo
import os

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

print(logo)


def caesar(start_text, shift, direction):
    alphabet_shift = []
    text = []

    if direction == "encode":
        for i in range((shift + 1), len(alphabet)):
            alphabet_shift.append(alphabet[i])

        for i in range(shift + 1):
            alphabet_shift.append(alphabet[i])

        for letter in start_text:
            if not letter.isalpha():
                text.append(letter)
            else:
                location = alphabet.index(letter)
                text.append(alphabet_shift[location - 1])

        print(f"The encoded text is '{''.join(text)}'.")

    elif direction == "decode":
        for i in range((len(alphabet) - shift), len(alphabet)):
            alphabet_shift.append(alphabet[i])

        for i in range((len(alphabet) - shift)):
            alphabet_shift.append(alphabet[i])

        for letter in start_text:
            if not letter.isalpha():
                text.append(letter)
            else:
                location = alphabet.index(letter)
                text.append(alphabet_shift[location])

        print(f"The decoded text is '{''.join(text)}'.")


option = False

while not option:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 26:
        shift = shift % 26

    caesar(text, shift, direction)

    option = input("Would you like to start over? Type 'yes' or 'no'.\n").lower()

    if option == "yes":
        option = False
        os.system("clear")
    elif option == "no":
        print("GoodBye!")
        option = True
    else:
        print("Invalid option")
