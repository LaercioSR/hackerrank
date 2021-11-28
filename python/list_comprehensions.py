if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    list_comprehensions = []
    for i_x in range(x+1):
        for i_y in range(y+1):
            for i_z in range(z+1):
                if (i_x + i_y + i_z) != n:
                    list_comprehensions.append([i_x, i_y, i_z])

    print(list_comprehensions)