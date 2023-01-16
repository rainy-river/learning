import random
import sys

answer = random.randint(1,20)
print('I am thinking of a number between one and twenty.')
while True:
    print('Take a guess.')
    guess = input()
    guess = int(guess)
    counter = 1
    if guess == answer:
        print('Good job! You guessed my number in ' + str(counter) + ' guesses!')
        sys.exit()
    elif guess < answer:
        print('Your guess is too low.')
        counter = counter + 1
        continue
    elif guess > answer:
        print('Youre guess is too high')
        counter = counter + 1
        continue