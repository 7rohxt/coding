if __name__ == '__main__':
    s = input()

    found_alnum = found_alpha = found_digit = found_lower = found_upper = False

    for char in s:
        if char.isalnum():
            found_alnum = True
        if char.isalpha():
            found_alpha = True
        if char.isdigit():
            found_digit = True
        if char.islower():
            found_lower = True
        if char.isupper():
            found_upper = True

        if found_alnum and found_alpha and found_digit and found_lower and found_upper:
            break

    print(found_alnum)
    print(found_alpha)
    print(found_digit)
    print(found_lower)
    print(found_upper)

    # alternative approach using any()
    
    # print(any(char.isalnum() for char in s))  
    # print(any(char.isalpha() for char in s))  
    # print(any(char.isdigit() for char in s))  
    # print(any(char.islower() for char in s))  
    # print(any(char.isupper() for char in s)) 