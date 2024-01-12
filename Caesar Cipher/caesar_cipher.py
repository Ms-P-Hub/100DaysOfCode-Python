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

option = False

while option == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def encrypt(text, shift):
        alphabet_shift = []
        encrypted_text = []

        for i in range((shift + 1), len(alphabet)):
            alphabet_shift.append(alphabet[i])

        for i in range(shift + 1):
            alphabet_shift.append(alphabet[i])

        for letter in text:
            location = alphabet.index(letter)
            encrypted_text.append(alphabet_shift[location - 1])

        print(f"The encoded text is '{''.join(encrypted_text)}'.")

    def decrypt(text, shift):
        alphabet_shift = []
        decrypted_text = []

        for i in range((len(alphabet)- shift), len(alphabet)):
            alphabet_shift.append(alphabet[i])

        for i in range((len(alphabet)- shift)):
            alphabet_shift.append(alphabet[i])

        for letter in text:
            location = alphabet.index(letter)
            decrypted_text.append(alphabet_shift[location])

        print(alphabet_shift)
        print(f"The decoded text is '{''.join(decrypted_text)}'.")

    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Invalid option")

    option = input("Would you like to start over? Type 'yes' or 'no'.\n").lower()

    if option == "yes":
        option = False
    elif option == "no":
        option = True
    else:
        print("Invalid option")
