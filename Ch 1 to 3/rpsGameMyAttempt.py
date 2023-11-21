import random

wins = 0
losses = 0
ties = 0

print('ROCK, PAPER, SCISSORS')

while True:
    print(str(wins) + ' Wins,' + str(losses) + ' Losses,' + str(ties) + ' Ties')
    print('Enter your move: (r)ock (p)aper (s)cissors')
    userMove = input()
    if userMove not in ['r','p','s']:
        print('That is not a valid move')
        continue
    if userMove == 'r':
        print ('ROCK versus ...')
    if userMove == 'p':
        print ('PAPER versus ...')
    if userMove == 's':
        print ('SCISSORS versus ...')   

    oppoMove = 'r'
    oppoInt = random.randint(0,2)
    if oppoInt == 1:
        oppoMove = 'p'
        print ('PAPER')
    if oppoInt == 2:
        oppoMove = 's'
        print ('SCISSORS')
    else:
        print ('ROCK')
        
    if userMove == oppoMove:
        ties = ties + 1
        print('It is a tie!')
    if userMove == 'r' and oppoMove == 's':
        print('You win!')
        wins = wins + 1
    elif userMove == 'p' and oppoMove == 'r':
        print('You win!')
        wins = wins + 1
    elif userMove == 's' and oppoMove == 'p':
        print('You win!')
        wins = wins + 1
    else:
        print('You lose!')
        losses = losses + 1


