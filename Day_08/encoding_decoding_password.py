'''
Exercise:4

# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

Solution: 

'''

num = [0,1,2,3,4,5,6,7,8,9]
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
special_symbol = ['!','@','#','$','%','^','&']

import random
number = input("Enter any number : ")
alpha_symbol = input("Enter any  alpha word: ").lower()
special_word = input("Enter any special symbol : ")

password_generate = []


