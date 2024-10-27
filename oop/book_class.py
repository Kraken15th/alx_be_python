class Book:
    """ Represents a book with title, author, and publication year. """
    def __init__(self, title, author, year):
        """Initializes a Book object with title, author, and publication year."""
        self.title = title
        self.author = author
        self.year = year
        def __del__(self):
            """ Prints a message upon object deletion. (Destructor) """
            print(f"Deleting {self.title}")
        def __str__(self):
                """Returns a user-friendly string representation of the book."""
                return f"{self.title} by {self.author}, published in {self.year}"
        def __repr__(self):
             """ Returns a string representation that can recreate the Book instance."""
             return f"Book('{self.title}', '{self.author}', {self.year})"
        if __name__ == "__main__":
             # Example usage (uncomment for testing without main.py)
             # my_book = Book("1984", "George Orwell", 1949)
             # print(my_book)
             # print(repr(my_book))
             # del my_book
             pass
        
