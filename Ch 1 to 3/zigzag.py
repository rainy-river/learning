import time, sys
indent = 0
indentIncreasing = True

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) #Pause for 1/10 sec

        if indentIncreasing:
            #Increase the number of spaces
            indent = indent + 1
            if indent == 20:
                #Change direction
                indentIncreasing = False
        else:
            #Decrease the number of spaces
            indent = indent - 1
            if indent == 0:
                #Change direction again
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()