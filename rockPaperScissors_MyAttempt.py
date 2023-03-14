import random
import sys

wins = 0
losses  = 0
ties = 0

while True:
    print(str(wins) + ' Wins, ' + str(losses) + ' Losses, ' + str(ties) + ' Ties')
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    playerMove = input()
    if playerMove == 'p':
        playerMove = 'PAPER'
    elif playerMove == 'r':
        playerMove = 'ROCK'
    elif playerMove == 's':
        playerMove = "SCISSORS"
    elif playerMove == 'q':
        sys.exit()
    else:
        print('Please enter a valid command.')
        continue

    computerMove = random.randint(1,3)
    if computerMove == 1:
        computerMove = 'PAPER'
    elif computerMove == 2:
        computerMove = 'ROCK'
    else:
        computerMove = 'SCISSORS'

    print(playerMove + ' versus...')
    print(computerMove)

    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif (playerMove == 'PAPER') and (computerMove == 'ROCK'):
        print('You win!')
        wins = wins + 1
    elif (playerMove == 'PAPER') and (computerMove == 'SCISSORS'):
        print('You lose.')
        losses = losses + 1
    elif (playerMove == 'ROCK') and (computerMove == 'SCISSORS'):
        print('You win!')
        wins = wins + 1
    elif (playerMove == 'ROCK') and (computerMove == 'PAPER'):
        print('You lose.')
        losses = losses + 1
    elif (playerMove == 'SCISSORS') and (computerMove == 'PAPER'):
        print('You win!')
        wins = wins + 1
    elif (playerMove == 'SCISSORS') and (computerMove == 'ROCK'):
        print('You lose.')
        losses = losses + 1
    else:
        print("Invalid result :(")
        continue
        





