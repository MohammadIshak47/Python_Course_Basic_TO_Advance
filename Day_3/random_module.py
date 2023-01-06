
### Random module 
'''
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
    

'''

# import random

# random_integer = random.randint(1, 10)
# print(random_integer)

## float
import random
random_float = random.random() ## it will give us value  between 0 to 1 (not 1)
print(random_float)

randomFloat = random.random()*5
print(random_float)

love_score = random.randint(1, 100)
print(f" Your love score is {love_score}")

