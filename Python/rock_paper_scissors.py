import random


def Roll1():
    rolling=input('Player 1, press the enter key to roll for either rock, paper or scissors')

def Roll2():
    rolling=input('Player 2, press the enter key to roll for either rock, paper or scissors')

def rps():
    game={1:'rock', 2:'paper', 3:'scissors'}
    Roll1()
    Choice1 = random.randint(1,3)
    Roll2()
    Choice2 = random.randint(1,3)

    print('Player 1 chose', game[Choice1] + '\n' + 'Player 2 chose', game[Choice2])

    if (Choice1 == game[1] and Choice2 == game[3]):
        print('Player 1 wins!')
    elif (Choice1 == game[3] and Choice2 == game[1]):
        print('Player 2 wins!')
    elif (Choice1 == Choice2):
        print("It's a draw!")
    elif (Choice1>Choice2):
        print('Player 1 wins!')
    else:
        print('Player 2 wins!')



rps()
