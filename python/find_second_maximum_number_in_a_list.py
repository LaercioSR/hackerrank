if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    set = []
        
    for x in arr:
        if x not in set:
            set.append(x)
    
    set.sort(reverse=True)
    print(set[1])