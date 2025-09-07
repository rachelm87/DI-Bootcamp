
from inheritance import Book
import os 

class Fiction(Book):
    def __init__(self, title, author, publication_date, price, is_awasome):
        super().__init__(title, author, publication_date, price)
        self.genre = 'Fiction'
        self.is_awasome = is_awasome

    def present(self):
        super().present()
        if self.is_awasome:
            print(f'genre: {self.genre}, is awasome? {self.is_awasome}')
        else:
            print('this book doesn\'t worth the info')


book2 = Fiction('Contact', 'Carl Sagan', 1995, 150, True)
book2.present()

book3 = Fiction('Fifty Shades of Grey', 'E.L. James', 2010, 5, False)
book3.present()