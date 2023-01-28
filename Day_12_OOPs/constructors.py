'''
Constructors

A constructor is a special method in a class used to create and initialize an object of 
a class. There are different types of constructors. Constructor is invoked automatically
 when an object of a class is created.

A constructor is a unique function that gets called automatically when an object is 
created of a class. The main purpose of a constructor is to initialize or assign values 
to the data members of that class. It cannot return any value other than None.
Syntax of Python Constructor

def __init__(self):
	# initializations

init is one of the reserved functions in Python. In Object Oriented Programming, it is 
known as a constructor.

Types of Constructors in Python

    Parameterized Constructor
    Default Constructor

Parameterized Constructor in Python

When the constructor accepts arguments along with self, it is known as parameterized 
constructor.

These arguments can be used inside the class to assign the values to the data members.
Example:

class Details:
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group

obj1 = Details("Crab", "Crustaceans")
print(obj1.animal, "belongs to the", obj1.group, "group.")

Output:

Crab belongs to the Crustaceans group.

Default Constructor in Python

When the constructor doesn't accept any arguments from the object and has only one 
argument, self, in the constructor, it is known as a Default constructor.
Example:

class Details:
  def __init__(self):
    print("animal Crab belongs to Crustaceans group")
obj1=Details()

Output:

animal Crab belongs to Crustaceans group

'''

# class Phone:
#     def __init__(self,brand,model,ram,rom):
#         self.brand = brand
#         self.model =  model
#         self.ram = ram
#         self.rom = rom
#     def full_specification(self):
#         return (f"Your phone brand is {self.brand} and model is {self.model}")


# phone1 = Phone('Samsung', 's23 ultra', '8GB', '4GB')

# print(phone1.full_specification())

class Dog:
    def __init__(self,name,color,fav_food):
        self.name = name
        self.color = color
        self.fav_food = fav_food

    def dog_details(self):
        return (f"My dog's name is {self.name} and color is {self.color}.It loves to eat {self.fav_food}")

    def update_name(self,name):
        self.name = name
        
    def update_color(self,color):
        self.color = color    

d1 = Dog('Tommy', 'brown', 'milk')
d2 = Dog('Dunki', 'white', 'rice')

print(d1.dog_details())

d1.update_name('Bonny')
d1.update_color('Red')

print(d1.dog_details())

print(d1.__dict__) ## it showing d1 object as dictionary
print(dir(d1)) ## here dir showing all my builtin methods,constructors





        

