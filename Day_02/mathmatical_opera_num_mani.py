'''
###### PEMDAS(rules of math which should first implement)
# P = Parenthesis ()
# E = Exponent (**)
# M = Multiplication (*)
# D = Division (/)
# A = Addition (+)
# S = Substraction (-)

# print(3*(3+3)/3-4)


## Problem_02: 
Instructions

Write a program that calculates the Body Mass Index (BMI) from a user's weight and 
height.The BMI is a measure of some's weight taking into account their height. e.g. 
If a tall person and a short person both weigh the same amount, the short person is 
usually more overweight.The BMI is calculated by dividing a person's weight (in kg) by 
the square of their height (in m):

Cannot infer image mime type

Warning you should convert the result to a whole number.
Example Input

weight = 80

height = 1.75

Example Output

80 ÷ (1.75 x 1.75) = 26.122448979591837

26

e.g. When you hit run, this is what should happen:

Cannot infer image mime type

Hint

    Check the data type of the inputs.
    Try to use the exponent operator in your code.
    Remember PEMDAS.
    Remember to convert your result to a whole number (int).


### Solution : 
BMI formula = weight (kg) / [height (m)]2  means height**2



'''

person_weight  = int(input("Enter your weight : "))
person_height =  int(input("Enter your height : "))

persons_total_measurement = (person_weight)/(person_height**2)

print("Person Measuremnt is : ",persons_total_measurement)






