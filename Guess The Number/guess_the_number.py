import random

print("Welcome to the Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

random_number = random.randint(1,100)

def easy():
    guesses = 10
    core_functionality(guesses)
        
def hard():
    guesses = 5
    core_functionality(guesses)
    
    
def core_functionality(guesses):
    print(f"You have {guesses} attempts remaining to guess the number.")
    while guesses > 0:
        guess = int(input("Make a guess: "))
        
        if guess > random_number :
            print("Too High\nGuess again")
            guesses -= 1
        elif guess < random_number:
            print("Too low\nGuess again")
            guesses -= 1
        else:
            print(f"You guessed correctly. Well Done! The answer is {random_number}")
            break
        print(f"You have {guesses} attempts remaining to guess the number.")
    print(f"You ran out of guesses. You lose! The answer was {random_number}")
        
if difficulty == 'easy':
    easy()
elif difficulty == 'hard':
    hard()
else:
    print("Invalid Input")