def printColor(c, s):
    print('\x1b[' + c + s + '\x1b[0m')

def inputColor(c, s):
    input('\x1b[' + c + s + '\x1b[0m')