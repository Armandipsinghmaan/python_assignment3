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
