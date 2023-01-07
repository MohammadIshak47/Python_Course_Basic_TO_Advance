
### Random module 
'''

# import random

# random_integer = random.randint(1, 10)
# print(random_integer)

## float
# import random
# random_float = random.random() ## it will give us value  between 0 to 1 (not 1)
# print(random_float)

# randomFloat = random.random()*5
# print(random_float)

# love_score = random.randint(1, 100)
# print(f" Your love score is {love_score}")


Problem_01:

Instructions

You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.

e.g. 1 means Heads 0 means Tails
Example Output

Heads

or

Tails

## Solution :
## 1 means Heads and 0 means Tails

import random

test_seed = int(input(" Create a seed number :  "))
random.seed(test_seed)

random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")    
    


### problem_02:
Instructions

You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.

Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name
Example Input

Angela, Ben, Jenny, Michael, Chloe

Note: notice that there is a space between the comma and the next name.
Example Output

Michael is going to buy the meal today!

Hint

    You might need the help of the len() function.

https://stackoverflow.com/questions/1712227/how-do-i-get-the-number-of-elements-in-a-list

    Remember that Lists start at index 0!

### Solution :
import random
test_seed = int(input("Create a seed number : "))
random.seed(test_seed)

namesAsCSV = input("Give me everybody's names separted by comma :  ")
names = namesAsCSV.split(',')

names_length = len(names)

random_choice = random.randint(0, names_length-1)
person_who_will_pay = names[random_choice]

print(f"{person_who_will_pay} is going to buy the meal!")



'''


# import random

# # namesCSV = input("Enter your names separted by comma: ")
# # names = namesCSV.split(",")

# person_who_will_pay = random.choice(names) ### by using choice function we can easily
# ## solve it
# print(f"{person_who_will_pay} is going to pay bill today")



# import random

# # namesCSV = input("Enter your names separted by comma: ")
# # names = namesCSV.split(",")
# names_length = len(names)

# namesLength = random.randint(0, names_length-1)
# person_who_will_pay = names[namesLength]

# print(f"{person_who_will_pay} is going to be pay bill.")


