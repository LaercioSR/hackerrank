if __name__ == '__main__':
    s = input()

    has_alnum = False
    has_alpha = False
    has_digit = False
    has_lower = False
    has_upper = False
    for c in s:
        has_alnum = has_alnum or c.isalnum()
        has_alpha = has_alpha or c.isalpha()
        has_digit = has_digit or c.isdigit()
        has_lower = has_lower or c.islower()
        has_upper = has_upper or c.isupper()

    print(has_alnum)
    print(has_alpha)
    print(has_digit)
    print(has_lower)
    print(has_upper)
