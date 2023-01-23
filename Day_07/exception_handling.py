'''
Exception Handling

Exception handling is the process of responding to unwanted or unexpected events when a computer program runs. Exception handling deals with these events to avoid the program or system crashing, and without this process, exceptions would disrupt the normal operation of a program.
Exceptions in Python

Python has many built-in exceptions that are raised when your program encounters an error (something in the program goes wrong).

When these exceptions occur, the Python interpreter stops the current process and passes it to the calling process until it is handled. If not handled, the program will crash.
Python try...except

try….. except blocks are used in python to handle errors and exceptions. The code in try block runs when there is no error. If the try block catches the error, then the except block is executed.
Syntax:

try:
     #statements which could generate 
     #exception
except:
     #Soloution of generated exception

Example:

try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")

Output:

Enter an integer: 6.022
Number entered is not an integer.


Finally Clause

The finally code block is also a part of exception handling. When we handle exception using the try and except block, we can include a finally block at the end. The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message.
Syntax:

try:
   #statements which could generate 
   #exception
except:
   #solution of generated exception
finally:
    #block of code which is going to 
    #execute in any situation

The finally block is executed irrespective of the outcome of try……except…..else blocks
One of the important use cases of finally block is in a function which returns a value.
Example:

try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")

Output 1:

Enter an integer: 19
Integer Accepted.
This block is always executed.

Output 2:

Enter an integer: 3.142
Number entered is not an integer.
This block is always executed.

'''
# try:
#     num = int(input("Enter any number : "))
#     print(num)

# except ValueError:
#     print("The number you have entered is not an integer.Please enter enter an integer value")



# try:
#     number = int(input("Enter your desired number : "))
#     a = [2,3,5]
#     print(a[number])
# except ValueError:
#     print("The number you have entered is not an integer")
    
# except IndexError:
#     print("Invalid index .list index out of range")


# try:
#     i = [1,3,5,6,7]
#     l = int(input("Enter your desired number : "))
#     print(i[l])

# except IndexError:
#     print('The number is out of range in list.')

# finally:
#     print("The above code is always executed.")    


def func():
    try:
        i = [1,3,5,6,7]
        l = int(input("Enter your desired number : "))
        print(i[l])
        return 1

    except IndexError:
        print('The number is out of range in list.')
        return 0

    finally:
        print("The above code is always executed.") 


print(func())