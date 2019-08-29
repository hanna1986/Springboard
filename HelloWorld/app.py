students_count = 1000
rating = 4.99
is_published = False
course_name = """
Multiple Lines
"""


x = 1
y = 2
x, y = 1, 2

x = y = 1

print(type(students_count))
# dynamic data types
age = 20
age = "Python"
print(age)

# type annotation, once declared an integer cannot assign a string, this will complain
# actually, didn't complain
age: int = 20
age = "Python"

# primitive types are immutable, the value cannot change, instead new address is allocated
x = 1
print(id(x))

x = x + 1
print(id(x))

# Mutable type. Lists are mutable
x = [1, 2, 3]  # list
print(id(x))

x.append(4)
print(id(x))

# Strings, also considered primitive, and therefore immutable
course = "Python Programming"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])  # only returns 0th, 1st, and second
print(course[:3])
print(course[0:])
print(course[:])

print(id(course))
print(id(course[0]))

# Escape Sequences
# \"
# \'
# \\
# \n
message = "Python \nProgramming"
print(message)
message = """
python
Programming
"""

print(message)

# Formatted Strings starts with f
first = "Mosh"
last = "Hamedani"
full = first+" "+last
# another way
full = f"{first} {last}" # inside curly braces will be evoluated at runtime, any expression is OK
print(full)

# useful string methods

course = "Python Programming"
print(course.upper())
print(course.lower())
print(course.title())

print(course.strip())

print(course.find("pro")) # returns -1
print(course.replace("P", "-"))

print("Programming" in course)
print("Programming" not in course)

# Numbers
x=10
x=0b10  
print(x)

print(bin(x))

x=0x12c
print(x)
print(hex(x))

# a+bi complex numbers
x = 1 + 2j
print(x)

# Arithmetic Operations
x = 10 + 3
x = 10 - 3
x = 10 * 3
x = 10 / 3
x = 10 // 3
x = 10 % 3
x = 10 ** 3

x = x + 1
x += 1
print(x)

import math

# Working with numbers
PI = 3.14
print(round(PI))
print(abs(PI))

print(math.floor(PI))

# Type Conversion, python is strongly typed, unlike Java, so in python we have to explicitly convert types
x = input("x: ")
#y = x+1 # python doesn't know whether x should be converted to number or 1 converted to a string

print(int(x))
print(float(x))
print(bool(x))
print(str(x))

# Falsy values are "" 0 [] None (null)
# everything else is True

# Conditional Statemenets
age = 22
if age >= 18:
    print("Adult")
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

print("All done!")

# Logical Operators
name = "Mosh"
if not name.strip():  # check is string is empty
    print("name is empty")


age = 22
if age >= 18 and age < 65:
    print("Eligible")


# 18 <= age < 65

if 18 <= age < 65:
    print("Eligible")

# Ternary Operator
age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"

# different way to rewrite the above code
message = "Eligible" if age >= 18 else "Not eligible"

print(message)

# For Loops, only for and while in python
for x in "Python":
    print(x)

for x in ['a', 'b', 'c']:
    print(x)

for x in range(5): # prints 0 to 4
    print(x)

for x in range(0, 10, 2): # prints 0, 2, 4, 6, 8
    print(x)

# range function does not return a list
print(type(range(5000000000))) # returns object of class 'range'
# range object can be iterated over


# For .. Else
names = ["John", "Mary"]
found = False
for name in names:
    if name.startswith("J"):
        print("Found")
        found = True
        break
if not found:
    print("Not found")

# another way
names = ["John", "Mary"]
for name in names:
    if name.startswith("J"):
        print("Found")
        break
else:
    print("Not found")

# while loops

guess = 0
answer = 5

while answer != guess:
    guess = int(input("Guess: "))

else:
    pass

# Functions

#number = [1, 2, 3] # list
#number = (1, 2, 3) # tuple, cannot modify
def increment(number: int, by: int = 1) -> tuple: # by is assigned default value
    return (number, number + by)



print(increment(1, by = 3)) # key word argument

# *args. wait, what?
def multiply(*list):   # when we add * before a parameter,
    total = 1        # python will see the parameter as a tuple
    for number in list:
        total *= number
    return total
print(multiply(2, 3, 4, 5))

# **args
def save_user(**user):  # makes it into a dictionary
    print(user)
    print(user["name"])

save_user(id=1, name = "admin")

# no block level scope
# there are local and global variables in context of functions

message = "a"
def greet():
    message = "b"
    print(message) 

greet() # prints b


message = "a"
def greet1():     # global variables are not changed in a function
    message = "b"

greet1()
print(message) # prints a


message = "a"
def greet2():     # use word global to change a global variable
    global message  # this is a bad practice
    message = "b"

greet2()

print(message) # prints b
# Debugging


def fizz_buzz(input):
    if (input%3 == 0) and (input%5 == 0):
        return "fizz_buzz"
    elif (input%3 == 0):
        return "fizz"
    elif (input%5 == 0):
        return "buzz"
    else:
        return input

print(fizz_buzz(1))











































































