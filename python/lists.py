if __name__ == '__main__':
    array = []
    N = int(input())
    for x in range(N):
        command = input()
        arguments = command.split(' ')
        if arguments[0] == 'insert':
            array.insert(int(arguments[1]), int(arguments[2]))
        elif arguments[0] == 'print':
            print(array)
        elif arguments[0] == 'remove':
            array.remove(int(arguments[1]))
        elif arguments[0] == 'append':
            array.append(int(arguments[1]))
        elif arguments[0] == 'sort':
            array.sort()
        elif arguments[0] == 'pop':
            array.pop()
        elif arguments[0] == 'reverse':
            array.reverse()