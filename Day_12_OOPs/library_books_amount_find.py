'''
Write a Library class with no_of_books and books as two instance variables. Write a 
program to create a library from this Library class and show how you can print all books,
add a book and get the number of books using different methods. Show that your program 
doesnt persist the books after the program is stopped!

'''

## Solution :

class Library:
    no_of_books = 0
    def __init__(self,name,price):
        self.name = name
        self.price = price
        Library.no_of_books+=1

    def books_info(self):
        return (f"Your choosen books name is {self.name} and price is {self.price}tk.") 
    def add_books(self,new_book):
        self.new_book = new_book
    def get_no_of_books(self):
        self.no_of_books = no_of_books

book1 = Library('Python3', 330)
print(book1.books_info())