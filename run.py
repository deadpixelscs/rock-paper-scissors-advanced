import random

# Stores the amount of wins for the player and cpu
player_score = 0
cpu_score = 0

print("Game Version: 1.0.0")
print("Created by Pete Machin")
print()
print("Welcome to Rock, Paper, Scissors Advanced!!!")
print()


def player_option():
    """
    Allows the player to enter their option and then checks if
    the entered key is valid and then returns the players choice.
    """
    player_choice = input("Choose Rock, Paper, Scissors or Gun: ")
    if player_choice in ["Rock", "rock", "r", "R", "ROCK"]:
        player_choice = "r"
    elif player_choice in ["Paper", "paper", "p", "P", "PAPER"]:
        player_choice = "p"
    elif player_choice in ["Scissors", "scissors", "s", "S", "SCISSORS"]:
        player_choice = "s"
    elif player_choice in ["Gun", "gun", "g", "G", "GUN"]:
        player_choice = "g"
    else:
        print("Invalid input, please try again")
        player_option()
    return player_choice

def cpu_option():
    """
    Randomly picks a number between 0 - 3 and then matches the numbers to the
    corresponding cpu choice
    """
    cpu_choice = random.randint(0, 3)
    if cpu_choice == 0:
        cpu_choice = "r"
    elif cpu_choice == 1:
        cpu_choice = "p"
    elif cpu_choice == 2:
        cpu_choice = "s"
    elif cpu_choice == 3:
        cpu_choice = "g"
    return cpu_choice


while True:
    # Calls players option functions and stores the returned value
    player_choice = player_option()
    cpu_choice = cpu_option()
    print("")

    # Checks the possible winning conditions to pick who the winner is
    if player_choice == "r":
        if cpu_choice == "r":
            print("You chose Rock, the cpu chose Rock, it's a TIE!")
        elif cpu_choice == "p":
            print("You chose Rock, the cpu chose Paper, you LOST!")
            cpu_score += 1
        elif cpu_choice == "s":
            print("You chose Rock, the cpu chose Scissors, you WON!")
            player_score += 1
        elif cpu_choice == "g":
            print("You chose Rock, the cpu chose Gun, you LOST!")
            player_score += 1

    elif player_choice == "p":
        if cpu_choice == "r":
            print("You chose Paper, the cpu chose Rock, you WON!")
            player_score += 1
        elif cpu_choice == "p":
            print("You chose Paper, the cpu chose Paper, it's a TIE!")
        elif cpu_choice == "s":
            print("You chose Paper, the cpu chose Scissors, you LOST!")
            cpu_score += 1
        elif cpu_choice == "g":
            print("You chose Paper, the cpu chose Gun, you LOST!")
            cpu_score += 1
            
    elif player_choice == "s":
        if cpu_choice == "r":
            print("You chose Scissors, the cpu chose Rock, you LOST!")
            cpu_score += 1
        elif cpu_choice == "p":
            print("You chose Scissors, the cpu chose Paper, you WON!")
            player_score += 1
        elif cpu_choice == "s":
            print("You chose Scissors, the cpu chose Scissors, it's a TIE!")
        elif cpu_choice == "g":
            print("You chose Scissors, the cpu chose Gun, you LOST!")
            cpu_score += 1

    elif player_choice == "g":
        if cpu_choice == "r":
            print("You chose Gun, the cpu chose Rock, you LOST!")
            cpu_score += 1
        elif cpu_choice == "p":
            print("You chose Gun, the cpu chose Paper, you WON!")
            player_score += 1
        elif cpu_choice == "s":
            print("You chose Gun, the cpu chose Scissors, you WON!")
            player_score += 1
        elif cpu_choice == "g":
            print("You chose Gun, the cpu chose Gun, it's a TIE!")
    
    
    # Prints the latest scores
    print("")
    print(f"Player score: {player_score}")
    print(f"Computer score: {cpu_score}")
    print("")

    # Checks if the player wants to continue playing another round
    player_choice = input("Do you want to play again? (y/n)")
    if player_choice in ["YES", "Yes", "yes", "y", "Y"]:
        pass
    elif player_choice in ["NO", "No", "no", "n", "N"]:
        break
    else:
        break