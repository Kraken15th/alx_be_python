class Book:
   """Represents a book with title and author information."""
   def __init__(self, title, author):
      """Initializes a Book object with title and author."""
      self.title = title
      self.author = author
      def __str__(self):
         """Returns a string representation of the book (base for derived classes)."""
         return f"Book: {self.title} by {self.author}"
class EBook(Book):
         """Represents an eBook with additional file size attribute."""
         def __init__(self, title, author, file_size):
            """Initializes an EBook object by calling the Book constructor and adding file size."""
            super().__init__(title, author)  # Call Book constructor
            self.file_size = file_size
            def __str__(self):
               """Returns a string representation of the eBook with file size information."""
               return f"{super().__str__()} (EBook), File Size: {self.file_size}KB"
class PrintBook(Book):
               """Represents a printed book with additional page count attribute."""
               def __init__(self, title, author, page_count):
                  """Returns a string representation of the PrintBook with page count information."""
                  return f"{super().__str__()} (PrintBook), Page Count: {self.page_count}"
class Library:
 """Represents a library with a collection of books."""
 def __init__(self):
      """Initializes a Library object with an empty list to store books."""
      self.books = []
      def add_book(self, book):
           """Adds a Book, EBook, or PrintBook instance to the library collection."""
           self.books.append(book)
           def list_books(self):
                """Prints details of each book in the library."""
                for book in self.books:
                     print(book)