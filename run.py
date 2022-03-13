import random               #imports a random module for this computer.

input("Welcome to a game of Rock, Paper, Scissors, Shield or Gwagg! Press Enter to start. ")

while True:
    player_choice = input("Rock, Paper, Scissors, Shield or Gwagg? ").lower()
    while player_choice != "rock" and player_choice != "paper" and player_choice != "scissors" and player_choice != "shield" and player_choice != "gwagg":
        player_choice = input("Invalid input, please try again: ").lower()


    random_num = random.randint(0,4)
    if random_num == 0:
        cpu_choice = "rock"
    elif random_num == 1:
        cpu_choice = "paper"
    elif random_num == 2:
        cpu_choice = "scissors"
    elif random_num == 3:
        cpu_choice = "shield"
    elif random_num == 4:
        cpu_choice = "gwagg"

    print()
    print("Your choice:", player_choice)
    print("Computer's choice:", cpu_choice)
    print()

    if player_choice == "rock":
        if cpu_choice == "rock":
            print("The game was a tie!")
        elif cpu_choice == "paper":
            print("You Lose!")
        elif cpu_choice == "scissors":
            print("You win!")
        elif cpu_choice == "shield":
            print("The game was a tie!")
        elif cpu_choice == "gwagg":
            print("You lost!")

    elif player_choice == "paper":
        if cpu_choice == "paper":
            print("The game was a tie!")
        elif cpu_choice == "rock":
            print("You Win!")
        elif cpu_choice == "scissors":
            print("You Lose!")
        elif cpu_choice == "shield":
            print("The game was a tie!")
        elif cpu_choice == "gwagg":
            print("You lost!")

    elif player_choice == "scissors":
        if cpu_choice == "scissors":
            print("The game was a tie!")
        elif cpu_choice == "rock":
            print("You Lose!")
        elif cpu_choice == "paper":
            print("You Win!")
        elif cpu_choice == "shield":
            print("The game was a tie!")
        elif cpu_choice == "gwagg":
            print("You lost!")

    elif player_choice == "shield":
        if cpu_choice == "shield":
            print("The game was a tie!")
        elif cpu_choice == "rock":
            print("The game was a tie!")
        elif cpu_choice == "paper":
            print("The game was a tie!")
        elif cpu_choice == "scissors":
            print("The game was a tie!")
        elif cpu_choice == "gwagg":
            print("The game was a tie!")

    elif player_choice == "gwagg":
        if cpu_choice == "gwagg":
            print("You Win!")
        elif cpu_choice == "rock":
            print("You Win!")
        elif cpu_choice == "paper":
            print("You Win!")
        elif cpu_choice == "scissors":
            print("You Win!")
        elif cpu_choice == "shield":
            print("The game was a tie!")


