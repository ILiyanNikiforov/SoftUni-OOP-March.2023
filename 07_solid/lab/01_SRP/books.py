class Library:
    def __init__(self, location):
        self.books = []
        self.location = location

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        try:
            self.books.remove(book)
        except ValueError:
            return "Book not in Library"

    def find_book(self, title):
        try:
            return [book for book in self.books if book.title == title][0]
        except IndexError:
            return "Book not found"


class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.location = location
        self.page = 0

    def turn_page(self, page):
        self.page = page


