'''
Recursion in python

Recursion is the process of defining something in terms of itself.
Python Recursive Function

In Python, we know that a function can call other functions. It is even possible for 
the function to call itself. These types of construct are termed as recursive functions.
Example:

def factorial(num): 
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1)) 
  
# Driver Code 
num = 7; 
print("Number: ",num)
print("Factorial: ",factorial(num))

Output:

number:  7
Factorial:  5040

'''



### Findout factorial number

# def factorial(n):
#     if (n ==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1)             

# num =  int(input("Enter your desired num : "))

# print(factorial(num))


### write a programe to findout fibonacci sequence

# Soluiton:

def fibbonacci(n):
    
    if n == 0:
        return 0
    elif n == 1 :
        return 1
    else:
        f1 = 0
        f2 = 1
        f3 = f1+f2
        f2 = f3


       
    return f3   

num = int(input("Enter your number : "))

print(fibbonacci(num))