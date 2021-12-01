def swap_case(s):
    modified_s = ''
    for i in s:
        if i >= 'a' and i <= 'z':
            modified_s += i.upper()
        elif i >= 'A' and i <= 'Z':
            modified_s += i.lower()
        else:
            modified_s += i
    return modified_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)