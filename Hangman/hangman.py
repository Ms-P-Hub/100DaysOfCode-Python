import random
import hangman_art as art
                   
print(art.logo)   
          
word_list = ["aardvark", "baboon", "camel"]

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
    break
  else:
    print(" ".join(hidden_list))
   
  if guess not in list_of_word:
    lives -=1
    print(art.stages[lives])
    if lives == 0:
      print(f"You Lose!\nThe word was {chosen_word}")