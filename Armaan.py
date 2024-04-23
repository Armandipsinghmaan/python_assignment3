#This is the Submission for the Library Managment System 
# The group members are 
# Armaandip singh maan 
# Manveer singh jandoo 
# Bhartinder singh 

import csv  # Importing the csv module for handling CSV files
import os.path  # Importing the os.path module for file path operations

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
        genre_names = {0: "Romance", 1: "Mystery", 2: "Science Fiction", 3: "Thriller", 4: "Young Adult",
                       5: "Children's fiction", 6: "Self-help", 7: "Fantasy", 8: "Historical Fiction", 9: "Poetry"}
        return genre_names.get(self.__genre, "Unknown Genre")

    # Get the availability status of the book
    def get_availability(self):
        return "Available" if self.__available else "Borrowed"

    # Setters to modify the values of private attributes
    def set_isbn(self, isbn):
        self.__isbn = isbn

    def set_title(self, title):
        self.__title = title

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
