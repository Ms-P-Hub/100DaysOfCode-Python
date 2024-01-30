with open("./Mail Merge/Input/Letters/starting_letter.txt",'r') as file:
    letter = file.read()

with open("./Mail Merge/Input/Names/invited_names.txt",'r') as file:
    names = file.readlines()

for i in names:
    name_inserted = letter.replace("[name]",i.strip("\n"))
    with open(f"./Mail Merge/Output/ReadyToSend/letter_to_{i}.txt",'w') as file:
        file.write(name_inserted)
