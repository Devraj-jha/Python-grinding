# Define the Book class
class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def __str__(self):
        # This method defines what the string representation of a Book object will be
        return f"'{self.title}' by {self.author}, published in {self.year_published}"

# Define the Library class
class Library:
    def __init__(self):
        self.books = []  # List to store books

    def add_book(self, book):
        # Method to add a book to the library
        self.books.append(book)

    def display_books(self):
        # Method to display all books in the library
        if self.books:
            for book in self.books:
                print(book)
        else:
            print("No books in the library.")

    def search_by_author(self, author):
        # Method to search books by author
        found_books = [book for book in self.books if book.author == author]
        if found_books:
            for book in found_books:
                print(book)
        else:
            print(f"No books found by {author}.")

# Create instances of the Book class
book1 = Book("The Catcher in the Rye", "J.D. Salinger", 1951)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book3 = Book("1984", "George Orwell", 1949)
book4 = Book("Animal Farm", "George Orwell", 1945)

# Create an instance of the Library class
library = Library()

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

# Display all books in the library
print("All books in the library:")
library.display_books()

# Search for books by George Orwell
print("\nBooks by George Orwell:")
library.search_by_author("George Orwell")

# Search for books by a non-existent author
print("\nBooks by J.K. Rowling:")
library.search_by_author("J.K. Rowling")
