alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        #  ['v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u']                       
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text , shift):
    alphabet_shift = []
    encrypted_text = []
    
    for i in range((shift+1),len(alphabet)):
        alphabet_shift.append(alphabet[i])
    
    for i in range(shift+1):
        alphabet_shift.append(alphabet[i])    
    
    for letter in text:
        location = alphabet.index(letter)
        encrypted_text.append(alphabet_shift[location-1])
    
    print(f"The encoded text is '{''.join(encrypted_text)}'.")
         
encrypt(text,shift)  
