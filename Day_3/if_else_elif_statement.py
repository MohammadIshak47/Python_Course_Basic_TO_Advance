'''
if-else Statements

Sometimes the programmer needs to check the evaluation of certain expression(s), whether the expression(s) evaluate to True or False. If the expression evaluates to False, then the program execution follows a different path than it would have if the expression had evaluated to True.

Based on this, the conditional statements are further classified into following types:

    if
    if-else
    if-else-elif
    nested if-else-elif.

An if……else statement evaluates like this:
if the expression evaluates True:

Execute the block of code inside if statement. After execution return to the code out of the if……else block.\
if the expression evaluates False:

Execute the block of code inside else statement. After execution return to the code out of the if……else block.
Example:

applePrice = 210
budget = 200
if (applePrice <= budget):
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")

Output:

Alexa, do not add Apples to the cart.

elif Statements

Sometimes, the programmer may want to evaluate more than one condition, this can be done using an elif statement.
Working of an elif statement

Execute the block of code inside if statement if the initial expression evaluates to True. After execution return to the code out of the if block.

Execute the block of code inside the first elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.

Execute the block of code inside the second elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.
.
.
.
Execute the block of code inside the nth elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.

Execute the block of code inside else statement if none of the expression evaluates to True. After execution return to the code out of the if block.
Example:

num = 0
if (num < 0):
    print("Number is negative.")
elif (num == 0):
    print("Number is Zero.")
else:
    print("Number is positive.")

Output:

Number is Zero.

Nested if statements

We can use if, if-else, elif statements inside other if statements as well.
Example:

num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")

Output:

Number is between 11-20


problem_01:

write a program that works out whether if a given number is an odd or even number.

Even numbers can be divided by 2 with no remainder.

e.g. 86 is even because 86 ÷ 2 = 43

43 does not have any decimal places. Therefore the division is clean.

e.g. 59 is odd because 59 ÷ 2 = 29.5

29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5,
 so the division is not clean.The modulo is written as a percentage sign (%) in Python. 
 It gives you the remainder after a division.

e.g.

6 ÷ 2 = 3 with no remainder.

6 % 2 = 0

5 ÷ 2 = 2 x 2 + 1, remainder is 1.

5 % 2 = 1

14 ÷ 4 = 3 x 4 + 2, remainder is 2.

14 % 4 = 2

Warning your output should match the Example Output format exactly, even the positions
of the commas and full stops.
Example Input 1

43

Example Output 1

This is an odd number.

Example Input 2

94

Example Output 2

This is an even number.

e.g. When you hit run, this is what should happen:

Cannot infer image mime type
Hint

    All even numbers can be divided by 2 with 0 remainder.
    Try some using the modulo with some odd numbers e.g.

3 % 2

5 % 2

7 % 2

Then try using the modulo with some even numbers e.g.

4 % 2

6 % 2

8 % 2

solution : 

number = int(input("Enter your number : "))


if number%2==0:
    print(number," is even number .")
else:
    print(number,"is odd number.") 



Excersice 2: Good Morning Sir

Create a python program capable of greeting you with Good Morning, Good Afternoon 
and Good Evening. Your program should use time module to get the current hour.
 Here is a sample program and documentation link for you:

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime


## Solution:

import time 

timestamp = time.strftime('%H:%M:%S ')

hour = int(time.strftime('%H'))

if 5<hour<12:
    print("Good morning sir")
elif 12<hour<15:
    print("Good noon sir")
elif 15<hour18:
    print("Good Afternoon sir")
elif 18<hour<19:
    print("Good Evening sir")
else:
    print("Good night sir")        





'''






   