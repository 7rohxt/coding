#Basic Data Types

# 1. Say "Hello, World!"
print("Hello, World!")

#--------------------------------------------------------------------------------------------------------
# 2. Python If-Else
if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")

#--------------------------------------------------------------------------------------------------------
# 3. Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)

#--------------------------------------------------------------------------------------------------------
# 4. Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)

#--------------------------------------------------------------------------------------------------------
# 5. Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i * i)

#--------------------------------------------------------------------------------------------------------
# 6. Write a Function
def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            leap = True
    return leap

#--------------------------------------------------------------------------------------------------------
year = int(input())
print(is_leap(year))

#--------------------------------------------------------------------------------------------------------
# 7. Print Function
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i + 1, end='')

#--------------------------------------------------------------------------------------------------------
# 8. List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    final = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print(final)

#--------------------------------------------------------------------------------------------------------
# 9. Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lis = list(arr)
    max_score = -float('inf')
    for i in lis:
        if i > max_score:
            max_score = i
    second_max = -float('inf')
    for i in lis:
        if i < max_score and i > second_max:
            second_max = i
    print(second_max)

#--------------------------------------------------------------------------------------------------------
# 10. Nested Lists
if __name__ == '__main__':
    records= []
    scores=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        i = [name,score]
        records.append(i)
        scores.append(i[1])
    
    # min_score = float('inf')
    # for j in scores:
    #     if j < min_score:
    #         min_score = j
    min_score = min(scores)
    
    second_min = min([k for k in scores if k > min_score])
    # second_min = float('inf')
    # for k in scores:
    #     if k > min_score and k<second_min:
    #         second_min = k
    
    second_lowest_students = sorted([n for n,s in records if s == second_min]) 
    
    for student in second_lowest_students:
        print(student)

#--------------------------------------------------------------------------------------------------------
# 11. Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    total = 0
    for name,marks in student_marks.items():
        if name==query_name:
            for i in marks:
                total += i
    

    print(f"{total/3:.2f}") 

#--------------------------------------------------------------------------------------------------------
# 12. Lists

if __name__ == '__main__':
    N = int(input())
    list1 = []
    for _ in range(N):
        cmd = input().split()   
        if cmd[0] =='insert':
            i=int(cmd[1])
            e=int(cmd[2])
            list1.insert(i,e)
        elif cmd[0] == 'print':
            print(list1)
        elif cmd[0] == 'remove':
            e = int(cmd[1])
            list1.remove(e)
        elif cmd[0] == 'append':
            e = int(cmd[1])
            list1.append(e)
        elif cmd[0] == 'sort':
            list1.sort()
        elif cmd[0] == 'pop':
            list1.pop()
        elif cmd[0] == 'reverse':
            list1.reverse()

#--------------------------------------------------------------------------------------------------------
# 13. Tuples

#python 2 
if __name__ == '__main__':
    n = int(raw_input()) # type: ignore
    integer_list = map(int, raw_input().split()) # type: ignore
    print(hash(tuple(integer_list)))

#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------

# STRINGS

# 14. sWAP cASE

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

#--------------------------------------------------------------------------------------------------------
# 15. String split and join

def split_and_join(line):
    input_list = line.split() 
    join = "-".join(input_list)
    return join
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#--------------------------------------------------------------------------------------------------------
# 16. Whats you name

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

#--------------------------------------------------------------------------------------------------------
# 17. Mutations

def mutate_string(string, position, character):
    string_list = list(string)
    # string_list[position] = character
    # string = "".join(string_list)
    string = string[:position]+character+string[position+1:]
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

#--------------------------------------------------------------------------------------------------------
# 18. Find a string

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

#--------------------------------------------------------------------------------------------------------
# 19. String Validators

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
#--------------------------------------------------------------------------------------------------------
# 20. Text Allignment 

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#--------------------------------------------------------------------------------------------------------
# 21. Text wrap

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

#--------------------------------------------------------------------------------------------------------