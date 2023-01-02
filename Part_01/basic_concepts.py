"""
## Every language has there grammatical rules .This rules are called syntax
## In computer data is nothing like binary numbers like 0 ,1 
### Data/values can be stored in temporary storage spaces called variables
### Variable is name associated and it is also address associate

## Example : 
num1 = 10 ## Here num1 is variable and 10 is value which is stored in our variable 
num2 = 20 
print(num1+num2)

## Decission making variable ... if else elif

### Looping statements are used to repeat a task in multiple times.

# Function is a block of code which performs a specific task. 
# Like Deposit_ Deposit is a function to deposit money,
# Withdraw __ it is a function to withdraw money
# Balance __ it is also a function to check money 

### class is a template/bluprint for real world entities 

## class has two behavior exist . 1_ is attribute/properties like mobile phone price , brand, model
color,battery life etc and 2_ is behavior/actions/methods like make a call , see videos,
send emails , calculate a number etc.

### Objects are specific instances of a class. Like phone is a class and it's specific instances
/object would be samsung, nokia , apple , oop etc. these are brand of phone clas which is object.

Example :  Samsung is an object  . it has different colors/battery life/price and using samsung 
can make a call , play games , watch videos . all the brand of mobile , it's attributes/property
and its methods/actions/behavior is comes together in one umbrella and it is called class.

### Algorithms__ step by step approach to solve a problem is known as algorithm
like <input> ...<steps to followed> ...<output>

how to make a glass of lemon juice?
step_01 : check if you have all the ingredient/elements
step_02 : Take lemon and cut into halves
step_03 : Squeeze lemon into a glass of water
step_04 : Add sugar and stir it well
step_05 : serve it cold with ice cubes


#### Python Tokens__python tokens is a smallest meaningful component in a program.There 
# are 4 types of tokens in python . such as _
1.Keywords
2.Identifiers
3. Literals
4.Operators ( +,-,*,/)

1. Keywords: Keywords are special reserved words . We cannot write Keywords as a variable .
 Example : class , def True , False ,and ,or ,not Yield, with ,while etc. 

2 . Identifiers :  Identifiers are names used for variables ,functions or objet .Rules__

i) No special character expect _(underscore)
ii) Identifiers are case sensative 
iii) First letter cannot be a digit

3 . Literals : Literals are constants in python .Constants don't change . Example
 a = 'Bangladesh' # bangladessh is string literals
 b = 123 ## here 123 is numerical literals


### String : strings are sequence of characters enclose within single qutoes(''), double qutoes(""
# or   triple qutoes(''' '''))

#### Data Structures in python : 1.Tuple 2.List 3. Set 4.Dictionary

1.Tuples : tuple is an ordered collection of elements enclosed with () .Tuples are immutable means
unchangeable . Once we create tuple . We cannot change inside of tuple values .
We can access every value of tuples like a[0].

2. List : list is an ordered collection of elements enclosed with [] . it is mutable . That means
it is changeable . like a[0] = 'bangladesh' . values inside list is changeable.



3.Dictionary : dictionary is an unordered collection of key-value pairs enclosed with {}
it is mutable, means it is changeable . We can change  the inside of the value of dictionary.

4. Set : set is an unordered and unindexed collection of elements enclosed with {}
Duplicates value are not ordered in set .


#### Loop : looping statements are used to repeat a task multiple times
For loop is used to iterate over a sequence(tuple,list,dictionary...) 



### string manipulation
a = 'Welcome to Beautiful Bangladesh . Nice to meet you everyone'
print(a.split(" ")) ## Here spilt method will separte in a list

print(a.replace('Bangladesh', 'village which name is Joarhamsadi'))

l1 = 'Hey'
l2 = 'there'
l3 = 'All'

# print(l1+ " " + l2 + ", " +  l3 +"!") ## Here it will print Hey there, All!
print('{} {}, {}!'.format(l1,l2,l3)) ## Here it will print Hey there, All!
print(f"{l1} {l2}, {l3}!") ## Here it will print Hey there, All!


####nested dictionary

# a = {'name':'Mohammad Ishak','gender':'Male','education':{'ssc':'2014','Hsc':'2016'},'age':'26'}

# # a[0] = 'Name'
# # print(a[0])

# print(a.pop('name'))
# print(a)
# print(a.popitem())
# print(a)

### Nested if 

# a = int(input("Enter your expected number:  "))

# if a<30:
#     if a%2==0:
#         print(a," is an even number and less than 30")
#     else:
#         print(a," is an odd number and  less than 30")    
# else:
#     print(a," is greater than 30")        

### findout vowel consonant

# a = input("Enter your character : ")

# if a in 'aeiouAEIOU':
#     print(a,'is vowel')
# else:
#     print(a,'is consonant')    

### Loop

# num = int(input("Enter multiple of 7 is "))

# while num%7!=0:
#     num = int(input("Enter multiple of 7 again is "))

# else:
#     print(num,"is multiple of 7 ")


#### matrix in nested loop

# matrix = [[1,2,3],[5,6,6]]

# for i in matrix:
#     for j in i:
#         print(j, end=' ') ## end = ' ' it remove spaces and by using it will not to able go to new line

#     print()    

### break statement

# string_word = ('Bangladesh is our motherland. We live in here')

# for i in string_word:
#     if i == '.': ## it find full-stop(.) if will be break and print before statement
#         break
#     print(i, end='')


### continue statement

# for i in [1,2,30,3,5,13,12,9] :
#     if i>12:
#         continue
#     print(i,end=',')

#### For loop

## suppose we will enter number 5 and it will show as:
#1
##12
#123
#12345

# n = int(input("Enter your number : "))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end= '')
#     print()    


### While loop
## 1 to 10 number summation is 55
# i = 1
# sum = 0

# while i<=10:
#     sum = sum+i
#     i+= 1
# print(sum)    

## Now 1 to 10 only even number summation will be 30 

# i = 1
# sum = 0
# while i<=10:
#     if i%2 == 0:
#         sum = sum+i
#     i+=1

# print(sum)

# print("Day-1 Python Print Function\n,The function is declared like this:\n What to print?")

### Function : 

# def numbers(*a):
#     total = 0
#     for i in a:
#         total = total+i
#     return total    
    
 


# print(numbers(2,3,4,5,5,6))


### class

# class Person:

#     def __init__(self,name,gender,age):
#         self.name = name
#         self.gender = gender
#         self.age = age

#     def talk(self):
#         return f"Hi, I am {self.name}"
#     def vote(self):
#         if self.age>=18:
#             print("You are allow to vote")
#         else:
#             print("You are not allowed to vote")



# person1 = Person('Mohammad Ishak', 'male', 18)
# person2 = Person('Ayisha', 'Female', 2)


# print(person1.talk())
# print(person2.vote())


## Thread

# from threading import*

# def show():
#     print("This is a child thread")

# t = Thread(target=show())
# t.start()
# print("This a parent thread")

"""

### Python Scripting

# import os

# def current_directory():
#     cwd = os.getcwd()
#     print(cwd)

# def file_path(filename):
#     path = os.path.abspath(filename)
#     print(path)

# current_directory()
# filename = 'sample.txt'
# file_path(filename)


####

# import time

# epc = time.time()
# print(epc)
# localtime  = time.localtime(epc)
# print(localtime)
# print(localtime.tm_year)
# print(time.ctime(epc))


#### Send email using smtp

# import smtplib
# smtobject = smtplib.SMTP('smtp.gmail.com',587)
# smtobject.ehlo()
# smtobject.starttls()
# smtobject.login('ishak1998bd@gmail.com', 'zwmfqzdebrsinjoa')
# smtobject.sendmail('ishak1998bd@gmail.com', 'ishakmiu47@gmail.com', 'Hey, I am Ishak')
# smtobject.quit()







