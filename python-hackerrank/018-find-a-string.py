def count_substring(string, sub_string):
    total = 0
        
    for i in range(len(string)):
        if string[i:len(sub_string)+i] == sub_string:
            total +=1
            
    return total

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)