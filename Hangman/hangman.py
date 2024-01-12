import random
import hangman_art as art
import hangman_words as words

print(art.logo)

word_list = words.word_list

chosen_word = random.choice(word_list)

list_of_word = list(chosen_word)

hidden_list = []

for i in list_of_word:
    hidden_list.append("_")


lives = 6

while lives != 0:
    print(" ".join(hidden_list))
    guess = input("\nGuess a letter: ").lower()

    if guess in hidden_list:
        print("Opps! You've already guessed that letter! Try again")

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            hidden_list[i] = guess

    if "_" not in hidden_list:
        print("You Win!")
        break

    elif guess not in list_of_word:
        lives -= 1
        print(f"{guess} is not in the word. You have {lives} lives remaining.")
        print(art.stages[lives])
        if lives == 0:
            print(f"You Lose!\nThe word was {chosen_word}.")
