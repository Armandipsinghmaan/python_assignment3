#This program is about the LIBRARY MANAGEMENT SYSTEM
# name of the project maker 
# Armaandip singh maan 
# Manveer singh jandoo
# Bhartinder singh 
# class - Object-Oriented Programming 

import csv
import os.path

# Define a Book class to represent a book object
class Book:
    def __init__(self, isbn, title, author, genre, available):
        # Initialize the attributes of the Book object
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__available = available

    # Getters to retrieve the values of private attributes
    def get_isbn(self):
        return self.__isbn

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_genre(self):
        return self.__genre

    # Get the name of the genre based on its ID
    def get_genre_name(self):
        genre_names = {
            0: "Romance",
            1: "Mystery",
            # Define genre names for different IDs
            # ...
        }
        return genre_names.get(self.__genre, "Unknown Genre")

    # Get the availability status of the book
    def get_availability(self):
        return "Available" if self.__available else "Borrowed"

    # Setters to modify the values of private attributes
    def set_isbn(self, isbn):
        self.__isbn = isbn

    def set_title(self, title):
        self.__title = title

    # Define similar setters for author, genre, and available

    # Method to mark the book as borrowed
    def borrow_it(self):
        if self.__available:
            self.__available = False
            return True
        else:
            return False

    # Method to mark the book as returned
    def return_it(self):
        if not self.__available:
            self.__available = True
            return True
        else:
            return False
        
#Bhartinder singh 
    # Static method to load books from a CSV file
    @staticmethod
    def load_from_csv(filename):
        if not os.path.exists(filename):
            print("File not found. Please try again.")
            return None
        books = []
        with open(filename, newline='') as csvfile:
            book_reader = csv.reader(csvfile, delimiter=',')
            next(book_reader)  # Skip the header row
            for row in book_reader:
                isbn, title, author, genre, availability = row
                # Convert genre ID to integer
                try:
                    genre_id = int(genre.strip())
                except ValueError:
                    genre_id = -1  # Default value for unknown genre
                # Convert availability to boolean
                is_available = availability.strip().lower() in ['true', '1', 't']
                # Create a new Book object and append to the list
                new_book = Book(isbn.strip(), title.strip(), author.strip(), genre_id, is_available)
                books.append(new_book)
        return books

    # Method to represent the Book object as a string
    def __str__(self):
        return f"{self.__isbn:<14} {self.__title:<25} {self.__author:<25} {self.get_genre_name():<20} {self.get_availability()}"

# Function to search for books based on a search value (title or author)
def search_book(books, search_value):
    found_books = [b for b in books if search_value.lower() in b.get_title().lower() or search_value.lower() in b.get_author().lower()]
    return found_books

# Function to borrow a book
def borrow_book(books, isbn):
    for b in books:
        if b.get_isbn() == isbn:
            if b.borrow_it():
                print(f"'{b.get_title()}' with ISBN {b.get_isbn()} successfully borrowed.")
            else:
                print(f"'{b.get_title()}' with ISBN {b.get_isbn()} is not currently available.")
            return
    print("No book found with that ISBN.")

# Function to return a borrowed book
def return_book(books, isbn):
    for b in books:
        if b.get_isbn() == isbn:
            if b.return_it():
                print(f"'{b.get_title()}' with ISBN {b.get_isbn()} successfully returned.")
            else:
                print(f"'{b.get_title()}' with ISBN {b.get_isbn()} is not currently borrowed.")
            return
    print("No book found with that ISBN.")

# Main function to run the library management system
def main():
    print("Starting the system ...")
    # Loop until a valid filename is provided
    while True:
        filename = input("Enter book catalog filename: ")
        books = Book.load_from_csv(filename)
        if books:
            print("Book catalog has been loaded.")
            break

#Manveer singh jandoo 
    # Main menu loop
    while True:
        print("\nReader's Guild Library - Main Menu")
        print("==================================")
        print("1. Search for books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("0. Exit the system")
        choice = input("Enter your selection: ")

        if choice == '1':
            # Search for books
            print("\n-- Search for books --")
            search_value = input("Enter search value: ")
            found_books = search_book(books, search_value)
            if found_books:
                # Print found books
                print("ISBN           Title                     Author                    Genre                Availability")
                print("-------------- ------------------------- ------------------------- -------------------- ------------")
                for book in found_books:
                    print(book)
            else:
                print("No matching books found.")
        elif choice == '2':
            # Borrow a book
            print("\n-- Borrow a book --")
            isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
            borrow_book(books, isbn)
        elif choice == '3':
            # Return a borrowed book
            print("\n-- Return a book --")
            isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
            return_book(books, isbn)
        elif choice == '0':
            # Exit the system
            print("\n-- Exit the system --")
            print("Good Bye!")
            break
        elif choice == '2130':  # Secret code to redirect to library menu
            import library_app
            library_app.main()
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
