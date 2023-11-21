def collatz(number):
    if (number % 2 == 0):
        even = int(number /2)
        print(even)
        return even
    else:
        odd = int(3 * number + 1)
        print(odd)
        return odd

while True:
    print('Please enter an integer:')
    try:
        cNum = input()
        cNum = int(cNum)
        while cNum != 1:
            cNum = collatz(cNum)
    except ValueError:
        print('That is not a valid integer')