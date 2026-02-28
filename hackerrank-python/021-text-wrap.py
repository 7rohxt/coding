import textwrap

def wrap(string, max_width):
    # string_list = list(string)
    
    # res = ''
    # for i,char in enumerate(string_list):
    #     if i % max_width == 0 and i !=0:
    #         res+="\n"
    #     res += char 

    # return res
    
    res = ""   
    for i in range(0,len(string),max_width):
        res = res + string[i:i+max_width] + "\n"
    return res

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)