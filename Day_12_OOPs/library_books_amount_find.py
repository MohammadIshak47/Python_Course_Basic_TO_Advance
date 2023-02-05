'''
Write a Library class with no_of_books and books as two instance variables. Write a 
program to create a library from this Library class and show how you can print all books,
add a book and get the number of books using different methods. Show that your program 
doesnt persist the books after the program is stopped!

'''

## Solution :

class Library:
    no_of_books = 0
    def __init__(self,name):
        self.name = name
        
        Library.no_of_books+=1

    def books_info(self):
        return (f"Your choosen books name is {self.name} and No of Books is {self.no_of_books}") 
    
book1 = Library('Python3')
print(book1.books_info())

book2 = Library('Machine Learning')
print(book2.books_info())