'''
data types : 
1. string
2. integer
3. float
4. boolean

name = len(input("What's your name : "))

# print("Your name "+name+" characters") ## Here it will show me TypeError because 
## it is concatenate only string ,not integer 

# print("Your name has "+str(name)+ " characters")
# print(f"Your name has {name} characters only")

### problem_01: Write a program that adds the digits in a 2 digit number. e.g. 
# if the input was 35, then the output should be 3 + 5 = 8

Warning. Do not change the code on lines 1-3. Your program should work for different 
inputs. e.g. any two-digit number.

### Solution : 

two_digit_num = input("Enter your desire numebr :  ")

total = int(two_digit_num[0])+int(two_digit_num[1])
print("Total of Two digit number is : ",total)

another way : 
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

#Check the data type of two_digit_number
# print(type(two_digit_number))

#Get the first and second digits using subscripting then convert string to int.
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

#Add the two digits together
two_digit_number = first_digit + second_digit

print(two_digit_number)

'''






