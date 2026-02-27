# 01 Exercise: Python Variables

# Q1. Calculate age using birth year and current year
birth_year = 2001
current_year = 2024
age = current_year - birth_year 
print("My age:", age)

# Q2. Store and print full name using first and last name
first_name = "Rohit"
last_name = "Karthick"
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# --------------------------------------------------------------------------------------------------------------------

# 02 Exercise: Numbers in Python

# Q1. Calculate the total area of a football field
field_length = 92 
field_width = 48.8 
total_area = field_length * field_width
print(f"The total area of the football field is {round(total_area, 1)} square meters.")

# Q2. Calculate change after purchasing 9 packets of chips
packets = 9
total_cost = round(packets * 1.49, 1)
change = 20 - total_cost
print(f"The shopkeeper will give me back {change} dollars.")

# Q3. Calculate total cost to replace tiles in a square bathroom
tile_length = 5.5
tile_area = round(pow(tile_length, 2), 2)
cost_per_sqft = 500
total_cost = cost_per_sqft * tile_area
print(f"The total cost to replace all tiles: {total_cost} Rs")

# Q4. Print the binary representation of the number 17
num = 17 
binary_representation = format(num, 'b')
print(f"Binary value of 17 is {binary_representation}")

# --------------------------------------------------------------------------------------------------------------------

# 03 Exercise: String in Python

# Q1. Create and print an address using + and f-string
street, city, country = "Dark Street", "Vellore", "India"
print(street + "\n" + city + "\n" + country)
print(f"{street} \n{city} \n{country}")

# Q2. Slice "revolves" and "sun" from the sentence
sentence = "Earth revolves around the sun"
print(sentence[6:14])  # "revolves"
print(sentence[-3:])   # "sun"

# Q3. Print daily fruit and vegetable intake
fruits, veggies = 2, 5
print(f"I eat {veggies} veggies and {fruits} fruits daily")

# Q4. Correct and print the sentence in one line
print("maine 200 banana khaye".replace("200", "10").replace("banana", "samosa"))

# --------------------------------------------------------------------------------------------------------------------

# 04 Exercise: Python Lists

# Q1.Monthly expenses: January-2200, February-2350, March-2600, April-2130, May-2190  
# Create a list to store these monthly expenses and using that, find out:

expenses = [2200, 2350, 2600, 2130, 2190]

# 1. In February, how many dollars did you spend extra compared to January?
print(f"1. In February, I spent {expenses[1] - expenses[0]} dollars more than January.")

# 2. Find out your total expense in the first quarter (first three months) of the year.
total_expense_q1 = sum(expenses[:3])
print(f"2. The total expense in the first quarter is {total_expense_q1}.")

# 3. June month just finished, and your expense is 1980 dollars. Add this item to the monthly expense list.
expenses.append(1980)
print(f"3. Expense list after including June: {expenses}")

# 4. You returned an item that you bought in April and got a refund of 200 dollars.
expenses[3] -= 200
print(f"4. The list after April refund: {expenses}")

# --------------------------------------------------------------------------------------------------------------------

# 05 Exercise: Python If Condition

# Q1. Using the following list of cities per country:

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

# 1. Write a program that asks the user to enter a city name and it should tell which country the city belongs to.
city = input("Enter a city name: ").strip().lower()
print(f"1. City Name: {city}")

if city in india:
    print("   Country: India")
elif city in pakistan:
    print("   Country: Pakistan")
elif city in bangladesh:
    print("   Country: Bangladesh")
else:
    print("   Choose from the cities listed above.")

# 2. Write a program that asks the user to enter two cities and it tells you if they both are in the same country or not.
city1 = input("Enter first city: ").strip().lower()
city2 = input("Enter second city: ").strip().lower()
print(f"2. City 1: {city1}, City 2: {city2}")

if city1 in india and city2 in india:
    print("   Both cities are in India.")
elif city1 in pakistan and city2 in pakistan:
    print("   Both cities are in Pakistan.")
elif city1 in bangladesh and city2 in bangladesh:
    print("   Both cities are in Bangladesh.")
else:
    print("   Both cities are in different countries.")

# Q2. Write a Python program that can tell you if your sugar level is normal or not.
# Normal fasting level sugar range is 80 to 100.
sugar_level = int(input("Enter your fasting sugar level: "))
print(f"Sugar level: {sugar_level}")

if sugar_level < 80:
    print("Status: Low Sugar")
elif sugar_level > 100:
    print("Status: High Sugar")
else:
    print("Status: Normal")

# --------------------------------------------------------------------------------------------------------------------

# 06 Exercise: Python for loop

# 1. Count occurrences of "heads" in the given result list.
result = ["heads", "tails", "tails", "heads", "tails", "heads", "heads", "tails", "tails", "tails"]
count_heads = sum(1 for i in result if i == "heads")
print(f"Heads: {count_heads} times")

# 2. Print squares of odd numbers from 1 to 10.
for i in range(1, 11, 2):
    print(f"The square of {i} is {i * i}")

# 3. Find the month corresponding to a given expense.
expense_list = [2340, 2500, 2100, 3100, 2980]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
expense = int(input("Enter the monthly expense: "))

if expense in expense_list:
    index = expense_list.index(expense)
    print(f"Matching Month: {months[index]}")
else:
    print("Expense Not Found")

# 4. Simulate a 5 km race with user input on tiredness.
for i in range(1, 6):
    response = input(f"Completed {i} km. Are you tired? (yes/no): ").strip().lower()
    if response == "yes":
        print("You did not finish the race")
        break
else:
    print("Congratulations! You finished the race!")

# 5. Write a program that prints following shape
# *
# **
# ***
# ****
# *****
for i in range(1, 6):
    print("*" * i)

# --------------------------------------------------------------------------------------------------------------------

# 07 Exercise: Functions in Python

# 1. Function to calculate area of a triangle.
def calculate_area(base, height):
    return 0.5 * base * height

b, h = 8, 10
print(f"Area: {calculate_area(b, h)}")

# 2. Modify function to calculate area of triangle or rectangle.
def calculate_area(base, height, shape='triangle'):
    if shape == 'triangle':
        return 0.5 * base * height
    elif shape == 'rectangle':
        return base * height

print(f"Triangle Area: {calculate_area(8, 10)}")
print(f"Rectangle Area: {calculate_area(8, 10, 'rectangle')}")

# 3. Function to print pattern based on input number.
def print_pattern(n):
    for i in range(1, n + 1):
        print("*" * i)

num = int(input("Enter an integer: "))
print_pattern(num)

# --------------------------------------------------------------------------------------------------------------------

# 08 Exercise: Python Dict and Tuples

# 1. Dictionary operations for country population
countries = {'China': 143, 'India': 136, 'USA': 32, 'Pakistan': 21}

action = input("Enter an action (print, add, remove, query): ").lower()

if action == 'print':
    for country, population in countries.items():
        print(f"{country} ==> {population}")

elif action == 'add':
    country = input("Enter country name: ")
    if country in countries:
        print(f"{country} already exists.")
    else:
        population = int(input("Enter population: "))
        countries[country] = population
        print(f"Updated: {countries}")

elif action == 'remove':
    country = input("Enter country name: ")
    if country in countries:
        del countries[country]
        for country, population in countries.items():
            print(f"{country} ==> {population}")
    else:
        print("Country not found.")

elif action == 'query':
    country = input("Enter country name: ")
    print(f"Population of {country}: {countries.get(country, 'Not found')} crores")

# 2. Stock prices operations
stocks = {'info': [600, 630, 620], 'ril': [1430, 1490, 1567], 'mtl': [234, 180, 160]}

action = input("Enter an action (print, add): ").lower()

if action == 'print':
    for stock, prices in stocks.items():
        avg = sum(prices) / len(prices)
        print(f"{stock} ==> {prices} ==> avg: {avg:.2f}")

elif action == 'add':
    stock = input("Enter stock name: ")
    price = int(input("Enter price: "))
    stocks.setdefault(stock, []).append(price)
    print(f"Updated: {stocks}")

# 3. Circle calculations
def circle_calc(radius):
    area = round(3.14 * radius ** 2, 2)
    circumference = round(2 * 3.14 * radius, 2)
    diameter = 2 * radius
    return area, circumference, diameter

radius = float(input("Enter radius: "))
area, circumference, diameter = circle_calc(radius)
print(f"Area: {area}, Circumference: {circumference}, Diameter: {diameter}")

# --------------------------------------------------------------------------------------------------------------------

# 09 Exercise: Python Read Write File

# 1. Find words with maximum occurrence in a file
with open("C:\\code\\Python_Basics\\Data Files\\poem.txt", "r") as f:
    text = f.read()

word_counts = {}
for word in text.split():
    word_counts[word] = word_counts.get(word, 0) + 1

max_count = max(word_counts.values())

print(f"Words with max occurrences ({max_count} times):")
for word, count in word_counts.items():
    if count == max_count:
        print(word)

# 2. Process stock data and calculate financial metrics
import csv

input_file = "C:\\code\\Python_Basics\\Data Files\\stocks.csv"
output_file = "C:\\code\\Python_Basics\\Data Files\\stocks_output.csv"

with open(input_file, "r") as fin, open(output_file, "w", newline="") as fout:
    reader = csv.reader(fin)
    writer = csv.writer(fout)

    header = next(reader)  # Skip header
    writer.writerow(["Company Name", "PE Ratio", "PB Ratio"])  # Write new header

    for row in reader:
        company, price, eps, book_value = row[0], float(row[1]), float(row[2]), float(row[3])
        pe_ratio = round(price / eps, 2)
        pb_ratio = round(price / book_value, 2)
        writer.writerow([company, pe_ratio, pb_ratio])

print("Stock financial metrics saved to:", output_file)

# --------------------------------------------------------------------------------------------------------------------

# 10 Exercise: Class and Objects

# 1. Define Employee class with id and name attributes
class Employee:
    def __init__(self, i, n):
        self.id = i
        self.name = n

emp = Employee(1, "coder")
print(vars(emp))

# 2. Delete id attribute and then the object
del emp.id
print(vars(emp)) 

del emp  # Deletes the entire object

# --------------------------------------------------------------------------------------------------------------------

# 11 Exercise: Inheritance

# 1. Create an Animal-Dog inheritance
class Animal:
    def __init__(self):
        print("Class Animal is Created")

    def habitat(self):
        return "Lives on land"

class Dog(Animal):
    def __init__(self):
        super().__init__()  # Calls the parent constructor
        print("Class Dog is Created")

    def sound(self):
        return "Barks"

# Create Dog object and test methods
dog = Dog()
print(dog.habitat())
print(dog.sound())

# --------------------------------------------------------------------------------------------------------------------

# 12 Exercise: Multiple Inheritance

# Create a multiple inheritance structure for Teacher, Student, and Youtuber.
# - A master's student can also be a Teacher (inherit from Teacher).
# - A student can also be a Youtuber (use multiple inheritance).

class Teacher:
    def __init__(self, name):
        self.name = name

    def teaches(self):
        print(f"{self.name} is a teacher\n")

class Student(Teacher): 
    def __init__(self, name, degree):
        super().__init__(name)
        self.degree = degree

    def teaches(self):
        if self.degree.lower() == "master's":
            super().teaches()

class Youtuber(Student):
    def __init__(self, name, degree, channel):
        super().__init__(name, degree)
        self.channel = channel

    def creates_content(self):
        print(f"{self.name} creates content on {self.channel} channel")

# Creating a Student who is also a Teacher
obj1 = Student("Rohit", "Master's")
obj1.teaches()

# Creating a Youtuber who is also a Student and Teacher
obj2 = Youtuber("Karthick", "Master's", "Code with Karthick")
obj2.creates_content()

# --------------------------------------------------------------------------------------------------------------------

# 13 Exercise: Raise Exception And Finally

# 1. Create a custom exception AdultException.
# 2. Create a class Person with attributes name and age in it.
# 3. Create a function get_minor_age() in the class. It throws an exception if the person is adult otherwise returns age.
# 4. Create a function display_person() which prints the age and name of a person.

class AdultException (Exception):
    pass


class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def get_minor_age(self):
        if int(self.age) > 18:
            raise AdultException("The person is an adult")
        else:
            return self.age
            
    def display_person(self):
        try:
            print(f"Age: {self.get_minor_age()}")
        except AdultException as e:
            print(f"Exception: {e}")
        finally:
            print(f"Name: {self.name}\n")

person1 = Person('Rohit',23)
print("Person 1")
person1.display_person()

person2 = Person('Karthick',11)
print("Person 2")
person2.display_person()

# --------------------------------------------------------------------------------------------------------------------

# 14 Exercise: Iterators

# 1. Create an iterator for fibonacci series in such a way that each next returns the next element from fibonacci series.
# 2. The iterator should stop when it reaches a `limit` defined in the constructor.

class Fibonacci():
    def __init__(self,limit = 50):
        self.a = 0
        self.b = 1
        self.limit = limit
    
    def __iter__(self):
        return self
    
    def __next__(self):
           if self.a > self.limit:
                raise StopIteration
           
           current = self.a 
           self.a, self.b = self.b, self.a + self.b  # Tuple unpacking technique 
           
           return current      

n = Fibonacci()
itr = iter(n)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

# --------------------------------------------------------------------------------------------------------------------

# 15 Exercise: Generators

# Print Square Sequence using yield
# Create Generator method such that every time it will returns a next square number

def NextSquareNumber():
    i = 1
    while True:
        yield i * i
        i += 1
    
for n in NextSquareNumber():
    if n > 25:
        break
    print(n)

# --------------------------------------------------------------------------------------------------------------------

# 16 Exercise: List Set Dict Comprehensions

# 1. Create a Dictionary which contains the Binary values mapping with numbers found in the below integer and binary and save it in binary_dict. 
integer = [0, 1, 2, 3, 4]
binary = ["0", "1", "10", "11", "100"]
z = zip(integer,binary)

binary_dict = {integer:binary for integer, binary in zip(integer,binary)}
print(binary_dict)

# 2. Create a List which contains additive inverse of a given integer list. 
integer=[1,-2,3,0,-6]
additive_inverse = [-i for i in integer]
print(additive_inverse)

# 3. Create a set which only contains unique sqaures from a given a integer list.
integer = [1, -2, 2, -3, 3, -4]
sq_set = set([i*i for i in integer])
print (sq_set)

# --------------------------------------------------------------------------------------------------------------------

# 17 Exercise: Sets and Frozen Sets

# 1. create any set and try to use frozenset(setname)

set = {'apple','banana','carrot','apple'}
fs = frozenset(set)
print(fs)

# 2. Find the elements in a given set that are not in another set

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(f"The elements in Set 1 which are not in Set 2 {set1 - set2}")
print(f"The elements in Set 2 which are not in Set 1 {set2 - set1}")

# --------------------------------------------------------------------------------------------------------------------

# 18 Exercise: Commandline Argument Processing using argparse

# 1. Take subject marks as command line arguments 

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

# --------------------------------------------------------------------------------------------------------------------

# 19 Exercise: Decorators

# 1. Create a decorator function to check that the argument passed to the function factorial is a non-negative integer:
# 2. Create a factorial function which finds the factorial of a number.
# 3. Use the decorator to decorate the factorial function to only allow factorial of non-negative integers.

def non_negative(func):
    def wrapper(*args, **kwargs):
      number = args[0]
      if number < 0 or  number % 1 != 0:
        return "The Number is a not a Positive Integer. Therefore, factorial cannot be performed."
      return func(*args, **kwargs)
    return wrapper

@non_negative
def factorial(number):
        fact = 1
        for i in range(1,int(number)+1):
            fact *= i
        return fact 

print(f"Number: 4  Factorial: {factorial(4)}")
print(f"Number: -3  Factorial: {factorial(-3)}")
print(f"Number: 2.3  Factorial: {factorial(2.3)}")

# --------------------------------------------------------------------------------------------------------------------

#20 Exercise: Multithreading

# 1. Create any multithreaded code using for loop for creating multithreads
# 2. Print total active threads in multithreaded code using threading.active_count()

import threading

def calculate_square(numbers):
    for n in numbers:
        print(f"Square: {n*n}")

arr = [2,4,7,9]

threads = []
for i in range(10):
    th = threading.Thread(target=calculate_square, args = (arr,))
    threads.append(th)
    th.start()

print(f"Active Threads: {threading.active_count()}")

for th in threads:
    th.join()

# --------------------------------------------------------------------------------------------------------------------
# The End