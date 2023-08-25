"""
@author : code8080.in

Let's create a program that simulates a basic library management system. This program will allow users to:

Add books to the library.
Borrow books from the library.
Return books to the library.
View available books.
In this program, we'll cover the following data types:

Strings (for book titles and author names)
Numbers (for book IDs)
Lists (for storing available and borrowed books)
Tuples (for representing a book with its title, author, and ID)
Dictionaries (for managing borrowed books with user names)
Sets (for ensuring unique book IDs)
Deque (from collections, for managing a queue of users waiting for a book)

"""
from collections import deque

class Library:
    def __init__(self):
        self.books = [
            (1, "Python Basics", "John Doe"),
            (2, "Advanced Python", "Jane Smith"),
            (3, "Data Structures in Python", "Alex Brown")
        ]
        self.borrowed_books = {}
        self.waiting_list = deque()

    def add_book(self, title, author):
        book_id = len(self.books) + 1
        self.books.append((book_id, title, author))
        print(f"Book '{title}' by {author} added with ID {book_id}.")

    def borrow_book(self, user, book_id):
        for book in self.books:
            if book[0] == book_id:
                self.books.remove(book)
                self.borrowed_books[user] = book
                print(f"{user} borrowed '{book[1]}'.")
                return
        print(f"Book with ID {book_id} is not available.")
        self.waiting_list.append(user)
        print(f"{user} added to the waiting list.")

    def return_book(self, user):
        if user in self.borrowed_books:
            book = self.borrowed_books.pop(user)
            self.books.append(book)
            print(f"{user} returned '{book[1]}'.")
            if self.waiting_list:
                next_user = self.waiting_list.popleft()
                print(f"Notify {next_user} that '{book[1]}' is now available.")
        else:
            print(f"{user} hasn't borrowed any books.")

    def view_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            print(f"ID: {book[0]}, Title: '{book[1]}', Author: {book[2]}")

def main():
    library = Library()
    while True:
        print("\nOptions:")
        print("1. View available books")
        print("2. Add a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            library.view_books()
        elif choice == "2":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)
        elif choice == "3":
            user = input("Enter your name: ")
            book_id = int(input("Enter book ID to borrow: "))
            library.borrow_book(user, book_id)
        elif choice == "4":
            user = input("Enter your name: ")
            library.return_book(user)
        elif choice == "5":
            print("Thank you for using the library system!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
