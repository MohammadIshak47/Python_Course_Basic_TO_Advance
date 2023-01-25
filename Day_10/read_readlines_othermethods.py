'''

readlines() method

The readline() method reads a single line from the file. If we want to read multiple 
lines, we can use a loop.

f = open('myfile.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)

The readlines() method reads all the lines of the file and returns them as a list of 
strings.
writelines() method

The writelines() method in Python writes a sequence of strings to a file. The sequence 
can be any iterable object, such as a list or a tuple.

Here's an example of how to use the writelines() method:

f = open('myfile.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()

This will write the strings in the lines list to the file myfile.txt. The \n characters 
are used to add newline characters to the end of each string.

Keep in mind that the writelines() method does not add newline characters between the 
strings in the sequence. If you want to add newlines between the strings, you can use a 
loop to write each string separately:

f = open('myfile.txt', 'w')
lines = ['line 1', 'line 2', 'line 3']
for line in lines:
    f.write(line + '\n')
f.close()

It is also a good practice to close the file after you are done with it.

'''
### readline() method

# f = open('myfile2.txt','r')
# i = 0
# while True:
#     i = i+1
#     line = f.readline()
#     if not line:
#         break

#     s1 = int(line.split(",")[0])
#     s2 = int(line.split(",")[1])
#     s3 = int(line.split(",")[2])

#     print(f"Marks of student {i} in Math is : {s1}")
#     print(f"Marks of student {i} in English is: {s2}")
#     print(f"Marks of student {i} in Physics is : {s3}")
#     print(line)


### writeline() method

# f = open('myfile2.txt','w')
# lines = ['line 1\n','line 2\n','line 3\n']
# f.writelines(lines)
# f.close()



### for loop to print unlimited lines
f = open('myfile2.txt','w')
lines = ['line 1\n','line 2\n','line 3\n']

for line in lines:
    f.write(line + '\n')

f.close()
