import random

while True:
    choices = ['rock', 'paper', 'scissors', 'shield', 'gwagg']

    cpu = random.choice(choices)
    player = None

    while player not in choices:
        player = input('rock, paper, scissors, shield or gwagg?: ').lower()

    if player == cpu:
        print('cpu:', cpu)
        print('player:', player)
        print('That games was a Tie!')

    elif player == 'rock':
        if cpu == 'paper':
            print('cpu:', cpu)
            print('player:', player)
            print('Hahahaha...You Lose!')
        if cpu == 'scissors':
            print('cpu:', cpu)
            print('player:', player)
            print('Welldone you beat me!')
        if cpu == 'shield':
            print('cpu:', cpu)
            print('player:', player)
            print('Unlucky!...close draw')
        if cpu == 'gwagg':
            print('cpu:', cpu)
            print('player:', player)
            print('Bye Bye')
        
    elif player == 'paper':
        if cpu == 'rock':
            print('cpu:', cpu)
            print('player:', player)
            print('Congratulations you won!')
        if cpu == 'scissors':
            print('cpu:', cpu)
            print('player:', player)
            print('Nevermind, you lose!')
        if cpu == 'shield':
            print('cpu:', cpu)
            print('player:', player)
            print('You Draw!')
        if cpu == 'gwagg':
            print('cpu:', cpu)
            print('player:', player)
            print('Bye Bye')

    elif player == 'scissors':
        if cpu == 'paper':
            print('cpu:', cpu)
            print('player:', player)
            print('Congratulations you won!')
        if cpu == 'rock':
            print('cpu:', cpu)
            print('player:', player)
            print('Nevermind, you lose!')
        if cpu == 'shield':
            print('cpu:', cpu)
            print('player:', player)
            print('You Draw!')
        if cpu == 'gwagg':
            print('cpu:', cpu)
            print('player:', player)
            print('Bye Bye')

    elif player == 'shield':
        if cpu == 'paper':
            print('cpu:', cpu)
            print('player:', player)
            print('You Draw!')
        if cpu == 'rock':
            print('cpu:', cpu)
            print('player:', player)
            print('You Draw!')
        if cpu == 'scissors':
            print('cpu:', cpu)
            print('player:', player)
            print('You Draw!')
        if cpu == 'gwagg':
            print('cpu:', cpu)
            print('player:', player)
            print('Kaaaching!...its a draw')

    elif player == 'gwagg':
        if cpu == 'paper':
            print('cpu:', cpu)
            print('player:', player)
            print('Welldone my friend!')
        if cpu == 'rock':
            print('cpu:', cpu)
            print('player:', player)
            print('Congratulations you won!')
        if cpu == 'scissors':
            print('cpu:', cpu)
            print('player:', player)
            print('Welldone you win!')
        if cpu == 'shield':
            print('cpu:', cpu)
            print('player:', player)
            print('Its a draw')

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break
print("Bye Bye!")


