'''
If ... Else in One Line

There is also a shorthand syntax for the if-else statement that can be used when the 
condition being tested is simple and the code blocks to be executed are short. Here's 
an example:

a = 2
b = 330
print("A") if a > b else print("B")

You can also have multiple else statements on the same line:
Example

One line if else statement, with 3 conditions:

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

Another Example

result = value_if_true if condition else value_if_false

This syntax is equivalent to the following if-else statement:

if condition:
    result = value_if_true
else:
    result = value_if_false

Conclusion

The shorthand syntax can be a convenient way to write simple if-else statements, 
especially when you want to assign a value to a variable based on a condition.
However, it's not suitable for more complex situations where you need to execute 
multiple statements or perform more complex logic. In those cases, it's best to use 
the full if-else syntax.

'''

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

print(f"The value of {a} is greater than {b}") if a>b else print(f"{a} is equal to {b}") if a == b else print(f"The value of {b} is greater than {a}")

