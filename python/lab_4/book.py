import random

MAX_BOOK_CODE = 10000


class Book:
    def __init__(self, book_name: str = None, author: str = None):
        if book_name == None:
            raise ValueError
        self.book_name = book_name
        self.author = author
        self.code = None

    def __repr__(self):
        return self.book_name + ' ' + self.author

    def tag(self):
        return [word for word in self.book_name.split() if word[0].isupper()]


class Library:
    book_codes = []

    def __init__(self, address: str, phone_number: str, listofbooks):
        self.address = address
        self.phone_number = phone_number
        self.availiblebooks = listofbooks

    def add(self, book):
        book.code = Library.generate_book_code()
        self.availiblebooks.append(book)

    @staticmethod
    def generate_book_code():
        code = random.randint(1, MAX_BOOK_CODE)
        while code in Library.book_codes:
            code = random.randint(1, MAX_BOOK_CODE)
        Library.book_codes.append(code)
        return code


lib = Library('St. Pushkina h. Kolotushkina 4', '+375291111111', [])
lib.add(Book('Harry Potter and the Deathly Hallows', 'J.K. Rowling'))
lib.add(Book('Life of Pi', 'Yann Martel'))
lib.add(Book('Lord of the Rings', 'J. R. R. Tolkien'))
print(lib.availiblebooks)
print(lib.book_codes)
print(lib.availiblebooks[0].tag())
Book()