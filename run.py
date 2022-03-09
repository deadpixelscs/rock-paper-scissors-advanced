import random

choices = ['rock','paper','scissors','gun']

cpu = random.choice(choices)
player = None

while player not in choices:
    player = input('rock, paper, scissors, or gun?: ')

if player == cpu:
    print('cpu: ',cpu)
    print('player: ',player)
    print('Unlucky!, that games was a Tie!')

elif player == 'rock':
    if cpu == 'paper':
        print('cpu: ',cpu)
        print('player: ',player)
        print('Hahahaha...You Lose!')
    if cpu == 'scissors':
        print('cpu: ',cpu)
        print('player: ',player)
        print('Welldone you beat me!')
    if cpu == 'gun':
        print('cpu: ',cpu)
        print('player: ',player)
        print('Welldone you won!')
        
elif player == 'paper':
    if cpu == 'rock':
        print('cpu: ',cpu)
        print('player: ',player)
        print('Congratulations you won!')
    if cpu == 'scissors':
        print('cpu: ',cpu)
        print('player: ',player)
        print('Nevermind, you lose!')
    if cpu == 'gun':
        print('cpu: ',cpu)
        print('player: ',player)
        print('You Lost!')

elif player == 'scissors':
    if cpu == 'paper':
        print('cpu: ',cpu)
        print('player: ',player)
        print('Congratulations you won!')
    if cpu == 'rock':
        print('cpu: ',cpu)
        print('player: ',player)
        print('Nevermind, you lose!')
    if cpu == 'gun':
        print('cpu: ',cpu)
        print('player: ',player)
        print('You Lost!')

elif player == 'gun':
    if cpu == 'paper':
        print('cpu: ',cpu)
        print('player: ',player)
        print('Congratulations you won!')
    if cpu == 'rock':
        print('cpu: ',cpu)
        print('player: ',player)
        print('Nevermind, you lose!')
    if cpu == 'scissors':
        print('cpu: ',cpu)
        print('player: ',player)
        print('Welldone you win!')