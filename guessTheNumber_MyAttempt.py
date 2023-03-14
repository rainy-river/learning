import random
import sys

answer = random.randint(1,20)
counter = 1
print('I am thinking of a number between one and twenty.')

while True:
    print('Take a guess.')
    guess = input()
    guess = int(guess)
    if (guess == answer) and (counter == 1):
        print('Great job!!! You guessed my number in a single guess!')
        sys.exit()
    elif guess == answer:
        print('Good job! You guessed my number in ' + str(counter) + ' guesses!')
        sys.exit()
    elif guess < answer:
        print('Your guess is too low.')
        counter = counter + 1
    elif guess > answer:
        print('Youre guess is too high')
        counter = counter + 1