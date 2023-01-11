'''
What are strings?

In python, anything that you enclose between single or double quotation marks is considered a string. A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters.
Example

name = "Harry"
print("Hello, " + name)

Output

Hello, Harry

Note: It does not matter whether you enclose your strings in single or double quotes, the output remains the same.

Sometimes, the user might need to put quotation marks in between the strings. Example, consider the sentence: He said, “I want to eat an apple”.

How will you print this statement in python?: He said, "I want to eat an apple". We will definitely use single quotes for our convenience

print('He said, "I want to eat an apple".')

Multiline Strings

If our string has multiple lines, we can create them like this:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

Accessing Characters of a String

In Python, string is like an array of characters. We can access parts of string by using its index which starts from 0.
Square brackets can be used to access elements of the string.

print(name[0])
print(name[1])

Looping through the string

We can loop through strings using a for loop like this:

for character in name:
    print(character)

Above code prints all the characters in the string name one by one!





#
print("Hi! My name is Mohammad Ishak\nI am a Backend Django Python Developer")
#
print("Hello, " + input("What's your name? ")) ## it will show Hello, Ishak(given name)
#
name = input("What is your name ?   ")
print(len(name))

###
a = input("a : ")
b = input("b : ")

print("a :",b)
print("b :",a)

#### simple string project
## problem : Creating your greeting for your program
## Ask the user for the city name where they grew up in
## Ask the user for the name of a pet
### combine the name of their city and pet name and show their band name.

## Solution: 
print("Welcome to the Band name Generator")
city_name = input("Whats the city you grew up in ? \n")
# print(city_name)
pet_name = input("What's your pet name?\n")
# print(pet_name)
print("Your brand name could be ",city_name,pet_name)


'''

# print("Hello brother , My name is \"Mohammad Ishak\".Are you ready to jump the race.")

# print("Bangladesh", "is", "our","motherland", sep='~') ## by using sep='~' it 
## will be separted word by word into ~ this symbol.

# print('Ishak','Faisal','Rasel','Irfan','Anas', end='00')

 






