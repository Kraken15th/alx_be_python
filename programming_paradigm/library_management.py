class Book:
    """ Represents a book in the library with title, author, and availability status."""
    def __init__(self, title, author):
        """ Initializes a Book object with title, author, and sets availability to True (not checked out)."""
        self.title = title
        self.author = author
        self._is_checked_out = True  # Private attribute for availability
    def check_out(self):
     """  Marks the book as checked out (unavailable). """
     self._is_checked_out = False
    def return_book(self):
       """ Marks the book as returned (available). """
       self._is_checked_out = True
    def is_available(self):
       """ Returns True if the book is available, False otherwise. """
       return self._is_checked_out
    def __str__(self):
      """ Returns a string representation of the book in a user-friendly format. """
      return f"{self.title} by {self.author}"
    class Library:
       """ Represents a library with a collection of Book objects and manages their availability. """
       def __init__(self):
          """ Initializes a Library object with an empty list to store books. """
          self._books = []
    def add_book(self, book):
       """ Adds a Book object to the library's collection. """
       self._books.append(book)
    def check_out_book(self, title):
       """Attempts to check out a book by title. If found and available, marks it as checked out."""
       for book in self._books:
          if book.title == title and book.is_available():
             book.check_out()
             print(f"Successfully checked out '{title}'.")
             return
          print(f"Book '{title}' not found or unavailable.")

    def return_book(self, title):
       """Attempts to return a book by title. If found, marks it as returned."""        
    for book in self._books:
     if book.title == title:
        book.return_book()
        print(f"Successfully returned '{title}'.")
        return
     print(f"Book '{title}' not found in the library.")
    def list_available_books(self):
       """Prints a list of all available books (checked out books are excluded)."""
       print("Available books:")
       for book in self._books:
          if book.is_available():
             print(book)
