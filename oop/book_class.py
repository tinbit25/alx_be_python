class Book:
    def __init__(self, title: str, author: str, year: int):
        """Initialize a Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that prints a deletion message."""
        print(f"Deleting {self.title}")

    def __str__(self) -> str:
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        """Return an official string representation of the book."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

# If you want to include a main section for testing within this file, you can uncomment below:
# if __name__ == "__main__":
#     my_book = Book("1984", "George Orwell", 1949)
#     print(my_book)  # Expected to use __str__
#     print(repr(my_book))  # Expected to use __repr__
#     del my_book