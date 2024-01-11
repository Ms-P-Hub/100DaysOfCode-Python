stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
                   
print(logo)             
word_list = ["aardvark", "baboon", "camel"]

import random
chosen_word = random.choice(word_list)

list_of_word =  list(chosen_word)
hidden_list = []

for i in list_of_word:
  hidden_list.append("_")
  
print(chosen_word)

lives = 6

while lives != 0:
  guess = input("\nGuess a letter: ").lower()

  for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
      hidden_list[i] = guess
      
  if "_" not in hidden_list:
    print("You Win!")
  else:
    print(" ".join(hidden_list))
   
  if guess not in list_of_word:
    lives -=1
    print(stages[lives])
    if lives == 0:
      print(f"You Lose!\nThe word was {chosen_word}")