
class Book:
    def __init__(self,  title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def check_out(self):
        self._is_checked_out = True
    def return_book(self):
        self._is_checked_out = False
    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, Book):
        self._books.append(Book)
        pass
    def check_out_book(self, title):
        for book in self._books:
            if (book.title == title):
                book.check_out()
                return
        print(f"A book {title} is already check out or not found!")

    def return_book(self, title):
        for book in self._books:
            if(book.title == title):
                book.check_in()
                return
        print(f"Book {title} already checked in or book not found")
        pass
    def list_available_books(self):
        for book in self._books:
            if not book._is_checked_out:
                print(book)
        pass