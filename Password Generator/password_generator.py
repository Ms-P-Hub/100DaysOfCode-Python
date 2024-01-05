import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


l_sequence = ""
for i in range(0,nr_letters):
    l_sequence += random.choice(letters)
    
n_sequence = ""
for i in range(0,nr_numbers):
    n_sequence += random.choice(numbers)

s_sequence = ""
for i in range(0,nr_symbols):
    s_sequence += random.choice(symbols)
    
password = l_sequence+n_sequence+s_sequence

print(f"Easy Password : {password}")

password_list = list(password)
random.shuffle(password_list)
print(f"Hard Password : {''.join(password_list)}")
    

