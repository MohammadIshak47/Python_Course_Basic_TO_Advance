'''
Snake Water Gun

Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where 
players use hand gestures to represent a snake, water, or a gun. The gun beats the snake,
the water beats the gun, and the snake beats the water. Write a python program to create
a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI.
Use proper functions to check for win.

'''


import random
def check(computer,user):
    if computer == user:
        return 0 
    if computer == 0 and user == 1:
        return -1 
    if computer == 1 and user == 2:
        return -1 
    if computer == 2 and user == 0:
        return -1 
    return 1                 
computer = random.randint(0, 2)
user = int(input("Choose Snake ,Water or Gun. 0 for Snake ,1 for Water,2 for Gun: "))

score = check(computer, user)

print("Your taken value :",user)
print("Computer taken value : ",computer)

if score == 0:
    print("It's draw")
elif score == -1:
    print("You lose")
else:
    print("Congrats,You win")    


