def swap_case(s):
    string_list = list(s)
    
    new_list = []
    for i in string_list:
        if i ==  i.lower():
            new_list.append(i.upper())            
        elif i == i.upper():
            new_list.append(i.lower())  
        else:
            new_list.append(i)  

    result = "".join(new_list)           
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)