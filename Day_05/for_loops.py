'''
### For loop

Introduction to Loops

Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops. Based on this loops are further classified into following main types;

    for loop
    while loop

The for Loop

for loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.
Example: iterating over a string:

name = 'Abhishek'
for i in name:
    print(i, end=", ")

Output:

A, b, h, i, s, h, e, k,
Example: iterating over a list:

colors = ["Red", "Green", "Blue", "Yellow"]
for x in colors:
    print(x)

Output:

Red
Green
Blue
Yellow

Similarly, we can use loops for lists, sets and dictionaries.
range():

What if we do not want to iterate over a sequence? What if we want to use for loop for a specific number of times?

Here, we can use the range() function.
Example:

for k in range(5):
    print(k)

Output:

0
1
2
3
4
Here, we can see that the loop starts from 0 by default and increments at each iteration.

But we can also loop over a specific range.
Example:

for k in range(4,9):
    print(k)

Output:

4
5
6
7
8


fruits = ["Apple","Banana","Orange","Mango"]

for fruit in fruits:
    print(fruit) ## it will print the list one by one items
    print(f"{fruit} pie")


print(fruits)

#### problem_01:
Instructions

You are going to write a program that calculates the average student height from a List of heights.

e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

The average height can be calculated by adding all the heights together and dividing by the total number of heights.

e.g.

180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

There are a total of 7 heights in student_heights

1146 ÷ 7 = 163.71428571428572

Average height rounded to the nearest whole number = 164

Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.
Example Input

156 178 165 171 187

In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]
Example Output

171

Hint

    Remember to use the round() function to round the average height before you print it.


## Solution :
 
 # student_heights = [180, 124, 165, 173, 189, 169, 146]
student_heights = input("Input a list of students heights : ").split()
for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])

print(student_heights) ### here print given input as a list


sum = 0
count = 0

for i in student_heights:
    sum = sum+i
    count +=1
    average_height = sum/count
    

print(sum)
print(round(average_height))



### problem_02:

Instructions

You are going to write a program that calculates the highest score from a List of scores.

e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

Important you are not allowed to use the max or min functions. The output words must match the example. i.e

    The highest score in the class is: x

Example Input

78 65 89 86 55 91 64 89

In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]
Example Output

The highest score in the class is: 91

Hint

    Think about the logic before writing code. How can you compare numbers against each other to see which one is larger?


'''


### Solution :




# student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

student_scores = input("Input a list of students scores: ").split()

for n in range(0,len(student_scores)):
    student_scores[n] = int(student_scores[n])

print(student_scores)

max_numbers = student_scores[0]
min_numbers = student_scores[0]

for number in student_scores:
    if number>max_numbers:
        max_numbers = number
    if number<min_numbers:
        min_numbers = number

print(f"The max numbers from the student score list is {max_numbers} ")
print(f"The min numbers from the student score list is {min_numbers}")


    

