def split_and_join(line):
    input_list = line.split() 
    join = "-".join(input_list)
    return join
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)