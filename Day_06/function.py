'''
### Function concept

A function is a block of code that performs a specific task whenever it is called. 
In bigger programs, where we have large amounts of code, it is advisable to create 
or use existing functions that make the program flow organized and neat.

There are two types of functions:

    Built-in functions
    User-defined functions

Built-in functions:

These functions are defined and pre-coded in python. Some examples of built-in functions
 are as follows:

min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.
User-defined functions:

We can create functions to perform specific tasks as per our needs. Such functions are 
called user-defined functions.
Syntax:

def function_name(parameters):
  pass
  # Code and Statements

    Create a function using the def keyword, followed by a function name, followed by a 
    paranthesis (()) and a colon(:).
    Any parameters and arguments should be placed within the parentheses.
    Rules to naming function are similar to that of naming variables.
    Any statements and other code within the function should be indented.

Calling a function:

We call a function by giving the function name, followed by parameters (if any) in 
the parenthesis.

Example:

def name(fname, lname):
    print("Hello,", fname, lname)

name("Sam", "Wilson")

Output:

Hello, Sam Wilson

# def add(num1,num2):

def add(*args):
    return args
    


add(44,33,34,66)
print(add())


# def CalculateGmean(a,b):
#     mean = (a*b)/(a+b)
#     return mean


# num1 = int(input("Enter num1 :"))
# num2 = int(input("Enter num2 :"))

# print(CalculateGmean(num1, num2))


def isGreater(a,b):
    if a>b:
        print(f"{a} is greater than {b}")
    else:
        print(f"{b} is greater than {a}")    


print(isGreater(1000, 90))

'''








