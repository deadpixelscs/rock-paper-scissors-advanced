import random

# Store wins for the player and cpu

player_score = 0
cpu_score = 0

choices = ["r", "p", "s", "g"]

def get_choice(input):
    """
    After presisng enter to begin the player can choose from one of the four
    options using the first letter of each choice on the keyboard. If the
    player no longer wishes to play they can Quit at anytime by
    pressing Q
    """
    if input == "r":
        return "Rock"
    elif input == "p":
        return "Paper"
    elif input == "s":
        return "Scissors"
    elif input == "g":
        return "Gun"


print("Game Version: 1.0.0")
print("Created by Pete Machin")
print()
print("Welcome to Rock, Paper, Scissors Advanced!!!")
print()
input("Press Enter to begin")
print()
print("[r] = Rock, [p] = Paper, [s] = Scissors, [h] =  Help and [q] = Quit\n")
counter = 1
while True:

    print("Game "+str(counter)+":")
    print("Please choose a letter:")
    player_choice = input()

    # Check to seee if the user wants to see the rules, if so select the Help
    if player_choice == "h":
        print("Rules go here")
        input("Press Enter when you are ready to begin: ")

    # Check that the user wants to quit the game and if so, then end the game.
    if player_choice == "q":
        print("Thanks for playing!...Please come back SOON!")
        break

# Allow the CPU to randomly pick one of the 4 choices.
    random_index = random.randint(0, 3)
    cpu_choice = choices[random_index]

    print("You selected "+get_choice(player_choice))
    print("The CPU selected "+get_choice(cpu_choice))

