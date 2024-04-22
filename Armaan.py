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
        
