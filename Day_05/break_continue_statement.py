'''
break statement

The break statement enables a program to skip over a part of the code.
 A break statement terminates the very loop it lies within.

example

for i in range(1,101,1):
    print(i ,end=" ")
    if(i==50):
        break
    else:
        print("Mississippi")
print("Thank you")

output

1 Mississippi
2 Mississippi
3 Mississippi
4 Mississippi
5 Mississippi
.
.
.
50 Mississippi


Continue Statement

The continue statement skips the rest of the loop statements and causes the next 
iteration to occur.

example

for i in [2,3,4,6,8,0]:
    if (i%2!=0):
        continue
    print(i)

output

2
4
6
8
0

'''

### break statement(it means stop the loop followed by condition)

# num = int(input("Enter your number : "))

# for i in range(1,12):
#     if i>10:
#         print("Stop the loop")
#         break
#     print(f"{num}x{i} = {num*i} ")
#     i+=1


### continue statement skip the iteration followed by condition
num = int(input("Enter your number : "))

for i in range(1,12):
    if i==10:
        print("Skip the iteration")
        continue
    print(f"{num}x{i} = {num*i} ")
    i+=1

   