import random

choices = ['rock','paper','scissors','gun']

cpu = random.choice(choices)
player = None

while player not in choices:
    player = input('rock, paper, scissors, or gun?: ')

print(player)

