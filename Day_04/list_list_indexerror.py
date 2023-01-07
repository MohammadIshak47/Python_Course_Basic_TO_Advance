'''
### List :A list is defined using square brackets and elements within them.
#  Each element is separated with the help of a comma.
## it is a mutable and ordered list.

list_name = [element_!, element_2, ..., element_n]

int_list= [3, 4, 5, 5, 6] # a list containing all integers
char_list = ['a', 'b', 'c', 'd'] # al list of characters
str_list = ["apple", 'banana', 'lemon', 'orange'] # a list of strings


##Using built-in function “reverse()”:
my_list = [45, 5, 33, 1, -9, 8, 76]
my_list.reverse()

###Reversing the list using -1
my_list = [45, 5, 33, 1, -9, 8, 76]
my_list[::-1]

####Removing Elements With Negative Index

Using the pop() function and giving -1 as parameter inside it we can remove the last 
element of that list and we get a new list.

my_list = [45, 5, 33, 1, -9, 8, 76]
my_list.pop(-1)
my_list


fruit_list = ["apple", 'banana', 'lemon', 'orange']
vegetable_list = ['cucumber','carrot','photato','radish']

combined_list = [fruit_list,vegetable_list]
print(combined_list)
## output will be [['apple', 'banana', 'lemon', 'orange'], ['cucumber', 'carrot', 'photato', 'radish']]



### problem_01: Treasure Map
Instructions

You are going to write a program which will mark a spot with an X.

In the starting code, you will find a variable called map.

This map contains a nested list. When map is printed this is what the nested list looks like:

['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']

In the starting code, we have used new lines (\n) to format the three rows into a square, like this:

['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']

This is to try and simulate the coordinates on a real map.

Your job is to write a program that allows you to mark a square on the map using a 
two-digit system. The first digit for the input will specify the column (the position 
on the horizontal axis). The second digit in the input will specify the row number 
(the position on the vertical axis).

First your program must take the user input and convert it to a usable format.

Next, you need to use it to update your nested list with an "x".
Example Input 1

column 2, row 3 would be entered as:

23

Example Output 1

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', 'X', '⬜️']

Example Input 2

column 3, row 1 would be entered as:

31

Example Output 2

['⬜️', '⬜️', 'X']

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']


Hint

    Remember that Lists start at index 0!
    map is just a variable that contains a nested list. It's not related to the map function in Python.


### Solution :
row1 = ["🔳","🔳","🔳"]
row2 = ["🔳","🔳","🔳"]
row3 = ["🔳","🔳","🔳"]

map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

horizontal_position = int(position[0])
vertical_position = int(position[1])

# selected_row = map[vertical_position-1]
# selected_row[horizontal_position-1] = 'X'

map[vertical_position-1][horizontal_position-1] = 'X'
print(f"{row1}\n{row2}\n{row3}")


'''



### project : Rock paper scissors
### Solution :


