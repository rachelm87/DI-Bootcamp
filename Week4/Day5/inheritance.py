#Review OOP - Inheritance

class Animal:

    def __init__(self, name):
        self.name = name
    
animal1 = Animal('Dog')

# print(animal1.name)


class Book:
    def __init__(self, title, author, publication_date, price):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.price = price

    def present(self):
        print(f'Title: {self.title}\n Author: {self.author}')





book1 = Book('1984', 'George Orwell', 1948, 100)
# book1.present()
# Book.present(book1)
