'''
Python Class and Objects

A class is a blueprint or a template for creating objects, providing initial values for 
state (member variables or attributes), and implementations of behavior 
(member functions or methods). The user-defined objects are created using the class 
keyword.
Creating a Class:

Let us now create a class using the class keyword.

class Details:
    name = "Rohan"
    age = 20

Creating an Object:

Object is the instance of the class used to access the properties of the class Now lets 
create an object of the class.
Example:

obj1 = Details()

Now we can print values:
Example:

class Details:
    name = "Rohan"
    age = 20

obj1 = Details()
print(obj1.name)
print(obj1.age)

Output:

Rohan
20


self parameter

The self parameter is a reference to the current instance of the class, and is used to 
access variables that belongs to the class.

It must be provided as the extra parameter inside the method definition.
Example:

class Details:
    name = "Rohan"
    age = 20

    def desc(self):
        print("My name is", self.name, "and I'm", self.age, "years old.")

obj1 = Details()
obj1.desc()

Output:

My name is Rohan and I'm 20 years old.

'''

# class Person:
#     name = "Ishak"
#     occupation = "Software Developer"
#     networth = 10
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")


# a = Person()
# b = Person()
# c = Person()

# a.name = "Rasel"
# a.occupation = "Accountant"

# b.name = "Faisal"
# b.occupation = "HR"

# # print(a.name, a.occupation)
# a.info()
# b.info()
# c.info()



# class Person:
#     def __init__(self,fname,lname,age,gender):
#         self.fname = fname
#         self.lname = lname
#         self.age = age
#         self.gender = gender

#     def full_name(self):
#         return (f"Your full name is {self.fname} {self.lname}") 


# person1 = Person('Mohammad', 'Ishak', 26, 'Male')

# print(person1.full_name())

