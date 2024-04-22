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

