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
# BMI formula = weight (kg) / [height (m)]2  means height**2

person_weight  = int(input("Enter your weight : "))
person_height =  float(input("Enter your height : "))

persons_bmi = person_weight/int(person_height*person_height)

print("Person Measuremnt is : ",int(persons_bmi))



print(round(9/2)) ## it will be integer value like four
print(round(11/2,2))
print(22//3) ## it will aslo give me integer value like 7

## f-string

name = 'Mohammad Ishak'
gener = 'Male'
profession = 'student'
Age = 26
nationality = 'Bangladeshi'

print(f"My name is {name} and my age is {Age}. I am a {gener} {profession} and I am {nationality}")


### problem_03:
Create a program using maths and f-Strings that tells us how many days, weeks, months we 
have left if we live until 90 years old.It will take your current age as the input and 
output a message with our time left in this format:
You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.

Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.
Example Input

56

Example Output

You have 12410 days, 1768 weeks, and 408 months left.


Hint

    There are 365 days in a year, 52 weeks in a year and 12 months in a year.
    Try copying the example output into your code and replace the relevant parts so that
     the sentence is formated the same way.


## Solution : 

living_age = int(input("Enter your existing age in earth : "))
present_age = int(input("Enter your present age : "))

remaining_age = living_age - present_age
remaining_days = remaining_age*365
remaining_weeks = remaining_age*52
remaining_months = remaining_age*12

print(f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left.")

#### Final project of Day_02:


'''

print("Welcome to the tip calculator")
total_bill = float((input("What was the total bill ? ")))
given_percentage = int(input("What percentage would you like to give? 10,12,15? "))
people_split = int(input("How many people to split the bill ? "))

total_bill_per_person = int(total_bill)/people_split
given_percentage_per_person = given_percentage/100

each_person_pay = total_bill_per_person*given_percentage_per_person
print("Each person should pay bill : ",float(each_person_pay))











