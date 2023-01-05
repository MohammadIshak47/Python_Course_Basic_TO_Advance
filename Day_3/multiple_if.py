'''
### problem_01 : 
## Solution : 
height = int(input('Enter your height : '))
photos_purpose_bill = 3
if height>=120:
    print("You can can ride .")
    age = int(input("Enter your age : "))
    if age>=18:
        adult_bill = int(input("Enter your bill $12: "))
        print(input("Do you want to photos? yes or no: "))
        if 'yes' or "Yes":
            print(f"Your total bill is ${adult_bill+photos_purpose_bill}")
        if 'no' or 'No':
            print(f"Your total bill is ${adult_bill}")    
    elif 12<=age<18:
        children_bill = int(input("Enter your bill $7:"))
        print(input("Do you want to photos? yes or no : "))
        if 'yes' or "Yes":
            print(f"Your total bill is ${children_bill+photos_purpose_bill}")
        if 'no' or 'No':
            print(f"Your total bill is ${children_bill}")    

    elif age<12:
        baby_bill = int(input("Enter your bill $5:"))
        print(input("Do you want to photos? yes or no : "))

        if 'yes' or "Yes":
            print(f"Your total bill is ${baby_bill+photos_purpose_bill}")
        if 'no' or 'No':
            print(f"Your total bill is ${baby_bill}")    

else:
    print("You can't ride .")    


### proble_02:
Congratulations, you've got a job at Python Pizza. Your first job is to build an 
automatic pizza order program. 
Based on a user's order, work out their final bill. 

```
Small Pizza: $15
```

```
Medium Pizza: $20
```

```
Large Pizza: $25
```

```
Pepperoni for Small Pizza: +$2
```

```
Pepperoni for Medium or Large Pizza: +$3
```

```
Extra cheese for any size pizza: + $1
```

# Example Input

```
size = "L"
```

```
add_pepperoni = "Y"
```

```
extra_cheese = "N"
```

# Example Output

```
Your final bill is: $28.
```

# Hint

1. Think about what you've learnt about multiple if statements and see if you can reduce
 the number of lines of code while having the same functionality.

### Solution :

print("Congratulations!,You've got a job at Python Pizza")

pizza_size = input("Your desired pizza size is(S ,M or L ):")
add_pepperoni = input("Do you add papperoni Y or N : ")
extra_cheese = input("Do you want to extra cheese Y or N : ")



pizza_bill = 0

if pizza_size == 'S':
    pizza_bill+=15
elif pizza_size == 'M':
    pizza_bill+=20
elif pizza_size == 'L':
    pizza_bill+=25
else:
    print('Your desired size is invalid . Please enter valid size')    

if add_pepperoni == 'Y':
    if pizza_size == 'S':
        pizza_bill+=2
    else:
        pizza_bill+=3
if extra_cheese == 'Y':
    pizza_bill+=1

print(f"Your final bill is ${pizza_bill}")


### problem_02: Love calculator

# Instructions

You are going to write a program that tests the compatibility between two people.  

To work out the love score between two people:

> Take both people's names and check for the number of times the letters in the word 
TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number. 


For Love Scores **less than 10** or **greater than 90**, the message should be:

`"Your score is **x**, you go together like coke and mentos."` 

For Love Scores **between 40** and **50**, the message should be:

`"Your score is **y**, you are alright together."`

Otherwise, the message will just be their score. e.g.:

`"Your score is **z**."`

e.g. 

`name1 = "Angela Yu"`

`name2 = "Jack Bauer"`

T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."

# Example Input 1

```
name1 = "Kanye West"
```

```
name2 = "Kim Kardashian"
```

# Example Output 1

```
Your score is 42, you are alright together.
```

# Example Input 2

```
name1 = "Brad Pitt"
```

```
name2 = "Jennifer Aniston"
```

# Example Output 2

```
Your score is 73.
```

e.g. When you hit **run**, this is what should happen:  

![](https://cdn.fs.teachablecdn.com/nfSILIPSNaIOwWhPR5vr)

The testing code will check for print output that is formatted like one of the lines below:
```
"Your score is 47, you are alright together."
"Your score is 125, you go together like coke and mentos."
"Your score is 54."
```

# Score Comparison

Not sure you're getting the correct score for the exercise? Use this table to check your code's score against mine.

| Name 1 | Name 2 | Score |
| --- | --- | --- |
Catherine Zeta-Jones | Michael Douglas |99
Brad Pitt |	Jennifer Aniston	| 73
Prince William	| Kate Middleton	| 67
Angela Yu	| Jack Bauer	| 53
Kanye West	| Kim Kardashian	| 42
Beyonce	| Jay-Z	| 23
John Lennon	| Yoko Ono	| 18

# Hint

1. The `lower()` function changes all the letters in a string to lower case. 

[https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python](https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python)

2. The `count()` function will give you the number of times a letter occurs in a string. 

[https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string](https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string)


### Solution :
print("Welcome to the Love Calcualator")

name1 = input("What's your name? \n")
name2 = input("What's their name? \n")

combined_name = name1+name2
lower_case_string = combined_name.lower()

t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')

true = t+r+u+e

l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')

love = l+o+v+e

love_score = int(str(true)+str(love))

if love_score<10 or love_score>90:
    print(f"Your total score is {love_score},you go together like coke and mentos.")
elif 40<=love_score<=50:
    print(f"Your total score is {love_score},you are alright together.")  
else:
    print(f"Your score is {love_score}")  


###problem :  Final project: treasure island game implement



# Solution :

# # print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/[TomekK]
# *******************************************************************************
# ''')

# print("Welcome to Treasure Island\nYour mission is to find the tresure.")
# choice1 =input("You're at a cross road.Where do you want to go? \"left\" or \"right\"").lower()

# if choice1== "left":
#     choice2 =input("You come to a lake.There is an island in the middle of the road.\nType \"wait\" to wait for a boat.Type \"swim\" to swim across.").lower()
#     if choice2 == 'wait':
#         choice3 =input("You arrived at the island unharmed.There is a house with 3 doors.\none red,one yellow,one blue.Which color do you choose? ").lower()
#         if choice3=='yellow':
#             print("Congrats!,You found the treasure .You win.")
#         else:
#             print("It's a room full of fire .Game over")    
#     else:
#         print("You got attacked by an angry trout.Game over")    


# else:
#     print('You fell into the hole.Game over')


