'''




## problem_01:
Instructions

You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:

i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.
Hint

    There are quite a few ways of solving this problem, but you will need to use the range() function in any of the solutions.

## Solution:

sum = 0
for i in range(2,101,2):
    sum+= i
print(f"final total is {sum}")  

### problem_02:

Instructions

You are going to write a program that automatically prints the solution to the FizzBuzz game.

    Your program should print each number from 1 to 100 in turn.

    When the number is divisible by 3 then instead of printing the number it should print "Fizz".

    `When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

      `And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`

e.g. it might start off like this:

`1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz`

.... etc.
Hint

    Remember your answer should start from 1 and go up to and including 100.

    Each number/text should be printed on a separate line.


Solution :


'''

for number in range(1,101):
    if number%3==0 and number%5==0:
        print("FizzBuzz")
    elif number%3==0:
        print("Fizz")
    elif number%5==0:
        print("Buzz")
       
    else:
        print(number)         

