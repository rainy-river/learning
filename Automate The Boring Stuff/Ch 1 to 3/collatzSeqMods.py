def collatz(number):
    if (number % 2 == 0):
        return number // 2
    else:
        return(3 * number + 1)
try:
    print('Enter an integer:')
    cNum = input()
    while cNum != 1:
        cNum = collatz(int(cNum))
        print(cNum)
except ValueError:
    print('That is not a valid integer')