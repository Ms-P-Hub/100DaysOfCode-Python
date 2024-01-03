print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
option_1 =  input("You're at a cross road. Where do you want to go? 'left' or 'right'\n")

if option_1 == "left":
    option_2 = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across\n")   
    if option_2 == "wait":
        option_3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n") 
        if option_3 == "red":
            print("It's a room full of fire. Game Over")
        elif option_3 == "blue":
            print("You enter a room of beasts. Game Over.")
        elif option_3 == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")    