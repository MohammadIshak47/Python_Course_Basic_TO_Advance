'''
Raising Custom errors

In python, we can raise custom errors by using the raise keyword.

salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")

In the previous tutorial, we learned about different built-in exceptions in Python and 
why it is important to handle exceptions. However, sometimes we may need to create our 
own custom exceptions that serve our purpose.
Defining Custom Exceptions

In Python, we can define custom exceptions by creating a new class that is derived from 
the built-in Exception class.

Here's the syntax to define custom exceptions:

class CustomError(Exception):
  # code ...
  pass

try:
  # code ...

except CustomError:
  # code...

This is useful because sometimes we might want to do something when a particular 
exception is raised. For example, sending an error report to the admin, calling an api,
 etc.

'''



# num = int(input("Enter your value between 10 and 20 : "))
# print(num)
# if (num<10 or num>20):
#     raise ValueError("Invalid input. Please enter number between 10 and 20.")


## Defining custom exceptions

class CustomError(Exception):
    def __init__(self,fname,laname):
        self.fname = fname
        self.laname = laname
    def full_name(self):
        return (f"Your full name is {self.fname}{self.laname}")
try:
    name = CustomError('Mohammad', ' Ishak')
    print(name.full_name())
except Exception:
    print('Invalid input.You are entered number. Please enter only string')               

