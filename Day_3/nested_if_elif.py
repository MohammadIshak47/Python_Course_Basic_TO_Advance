'''
### Nested if else elif

height = int(input("Enter your current height  : "))


if height>=120:
    print("You can ride Rollercoaster")
    age = int(input("Enter your current age : "))
    if age>18:
        print("You have to pay $12")
    elif 12<=age<=18:
        print("You have to pay $7 ")    
    else:
        print("You have to pay $5")    

else:
    print("You can't ride the rollercoster. Before ride you should grow over 120cm")

##problem_02 :
Instructions

Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

    Under 18.5 they are underweight
    Over 18.5 but below 25 they have a normal weight
    Over 25 but below 30 they are slightly overweight
    Over 30 but below 35 they are obese
    Above 35 they are clinically obese.


The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

Cannot infer image mime type

Warning you should round the result to the nearest whole number. The interpretation message needs to include the words in bold from the interpretations above. e.g. underweight, normal weight, overweight, obese, clinically obese.
Example Input

weight = 85

height = 1.75

Example Output

85 ÷ (1.75 x 1.75) = 27.755102040816325

Your BMI is 28, you are slightly overweight.

e.g. When you hit run, this is what should happen:

Cannot infer image mime type

The testing code will check for print output that is formatted like one of the lines below:

"Your BMI is 18, you are underweight."
"Your BMI is 22, you have a normal weight."
"Your BMI is 28, you are slightly overweight."
"Your BMI is 33, you are obese."
"Your BMI is 40, you are clinically obese."

Hint

    Try to use the exponent operator in your code.
    Remember to round your result to the nearest whole number.
    Make sure you include the words in bold from the interpretations.


Solution : 
height = float(input("Enter your height : "))
weight = int(input("Enter your weight : "))

bmi = weight/int((height*height))


if bmi<18.5:
    print(f"Your BMI is {bmi} & You are underweight")
elif 18.5<=bmi<25:
    print(f"Your BMI is {bmi} & You have normal weight")
elif 25<=bmi<30:
    print(f"Your BMI is {bmi} & You are slightly overweight")   

elif 30<=bmi<35:
    print(f"Your BMI is {bmi} & You are obese")
else:
    print(f"Your BMI is {bmi} & You are clinically obese.")

problem_03:

Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:

https://www.youtube.com/watch?v=xX96xng7sAE

This is how you work out whether if a particular year is a leap year.

    on every year that is evenly divisible by 4 **except** every year that is evenly divisible by 100 **unless** the year is also evenly divisible by 400

e.g. The year 2000:

2000 ÷ 4 = 500 (Leap)

2000 ÷ 100 = 20 (Not Leap)

2000 ÷ 400 = 5 (Leap!)

So the year 2000 is a leap year.

But the year 2100 is not a leap year because:

2100 ÷ 4 = 525 (Leap)

2100 ÷ 100 = 21 (Not Leap)

2100 ÷ 400 = 5.25 (Not Leap)

Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.
Example Input 1

2400

Example Output 1

Leap year.

Example Input 2

1989

Example Output 2

Not leap year.

e.g. When you hit run, this is what should happen:

Cannot infer image mime type
Hint

    Try to visualise the rules by creating a flow chart on www.draw.io
    If you really get stuck, you can see the flow chart I created:


solution :

year = int(input("Enter your Year : "))

if year%4==0:
    if year%100==0:
        if year%400==0:
         print(year," is Leap Year.")
        else:
          print(year," is not Leap Year") 
    else:
       print(year," is leap year")       
else:
   print(year," is  not Leap Year.") 


'''

                   

    

   
      


