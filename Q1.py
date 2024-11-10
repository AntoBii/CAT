class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"The book '{self.title}' is now marked as borrowed.")
        else:
            print(f"The book '{self.title}' is already borrowed.")

    def mark_as_returned(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"The book '{self.title}' is now marked as returned.")
        else:
            print(f"The book '{self.title}' is not currently borrowed.")

class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
            print(f"{self.name} has successfully borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is already borrowed by someone else.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned '{book.title}'.")
        else:
            print(f"{self.name} has not borrowed '{book.title}'.")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f" - {book.title} by {book.author}")
        else:
            print(f"{self.name} has not borrowed any books.")

# Interactive code to simulate borrowing and returning books

# Sample books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("1984", "George Orwell")
book3 = Book("To Kill a Mockingbird", "Harper Lee")

# Sample library member
member = LibraryMember("Alice", "M001")

# Menu for interaction
def library_menu():
    while True:
        print("\nLibrary Menu:")
        print("1. Borrow a Book")
        print("2. Return a Book")
        print("3. List Borrowed Books")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nAvailable books:")
            for book in [book1, book2, book3]:
                if not book.is_borrowed:
                    print(f" - {book.title} by {book.author}")
            
            title = input("Enter the title of the book you want to borrow: ")
            book = next((b for b in [book1, book2, book3] if b.title == title), None)
            if book:
                member.borrow_book(book)
            else:
                print("Book not found.")

        elif choice == '2':
            print("\nBorrowed books:")
            member.list_borrowed_books()
            
            title = input("Enter the title of the book you want to return: ")
            book = next((b for b in member.borrowed_books if b.title == title), None)
            if book:
                member.return_book(book)
            else:
                print("You haven't borrowed this book.")

        elif choice == '3':
            member.list_borrowed_books()

        elif choice == '4':
            print("Exiting the library menu.")
            break

        else:
            print("Invalid choice. Please try again.")

# Start the interactive menu
library_menu()
