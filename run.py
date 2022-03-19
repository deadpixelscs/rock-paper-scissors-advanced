import random

print()
print("Game Version: 1.0.0")
print("Created by Pete Machin")
print()
print("Welcome to Rock, Paper, Scissors Advanced!!!")
print()
input("Press Enter to start: ")
print()

player_score = 0
cpu_score = 0

# Game results

"""
placeholder

Args:
    placeholder

Returns:
    placeholder
"""

while True:

    outcomes = {
        "rock": {"rock": "0", "paper": "0", "scissors": "1", "gun": "1"},
        "paper": {"paper": "0", "rock": "1", "scissors": "0", "gun": "0"},
        "scissors": {"scissors": "0", "paper": "1", "rock": "0", "gun": "0"},
        "gun": {"gun": "0", "paper": "1", "scissors": "1", "rock": "0"},
    }

    def converted_outcome(number):
        if number == 0:
            return "rock"
        elif number == 1:
            return "paper"
        elif number == 2:
            return "scissors"
        elif number == 3:
            return "gun"

# Main loop
    while True:
        random_num = random.randint(0, 3)
        cpu_choice = converted_outcome(random_num)
        player_choice = input(str("Rock, Paper, Scissors or Gun? ")).lower()
        print()

        try:
            print("You selected : ", player_choice)
            print()
            print("The computer selected : ", cpu_choice)
            print()
            print("Game Outcome")
            print()
            print(outcomes[player_choice][cpu_choice])
            print("")
        except:
            print("--- INVALID INPUT!...Please try again: ---")
            print()
