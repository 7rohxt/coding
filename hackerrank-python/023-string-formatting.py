def print_formatted(number):
    # your code goes here

    width = len(bin(number)[2:])

    for i in range(1,number+1):   
        print (str(i).rjust(width)+str(oct(i)[2:]).rjust(width+1)+str(hex(i)[2:].upper()).rjust(width+1)+str(bin(i)[2:]).rjust(width+1))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)