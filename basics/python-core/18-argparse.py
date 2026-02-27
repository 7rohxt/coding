# Exercise: Commandline Argument Processing using argparse

# 1. Take subject marks as command line arguments 
# ```
# example: 
#     python3 cmd.py --physics 60 --chemistry 70 --maths 90
# ```
# 2. Find average marks for the three subjects using command line input of marks.


import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--physics", help="Physics Marks")
    parser.add_argument("--chemistry", help="Chemistry Marks")
    parser.add_argument("--maths", help="Maths Marks")
    parser.add_argument("--operation", help="Operation",  choices = ['average'] )

    args = parser.parse_args()

    print(args.physics)
    print(args.chemistry)
    print(args.maths)
    print(args.operation)

    m1=int(args.physics)
    m2=int(args.chemistry)
    m3=int(args.maths)
    average = None
    if args.operation == 'average':
        average = (m1+m2+m3)/3
    else:
        print("Unsupported Operation")
    
    print(f"Average: {average}")

# Output

# c:\code\Python_Basics>python 18_Argparse.py --physics 60 --chemistry 70 --maths 90 --operation average
# 60
# 70
# 90
# average
# Average: 73.33333333333333