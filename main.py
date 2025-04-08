from library import Library
from book import Book
from digitalbook import DigitalBook
from magazine import Magazine

def main():
    library = Library("Smart City Library")

    # Add various book types to the library
    library.add_book(Book("Atomic Habits", "James Clear", 2018))
    library.add_book(DigitalBook("Learn Python", "Guido van Rossum", 2021, 90))
    library.add_book(Magazine("Tech Monthly", "Editorial Board", 2024))

    while True:
        print("\n📚 WELCOME TO THE SMART LIBRARY 📚")
        print("1. View All Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Rate a Book")
        print("5. Exit")

        choice = input("Choose an option (1–5): ")

        if choice == "1":
            print("\nLibrary Catalog:")
            for book in library.books:
                print("-", book.get_details())

        elif choice == "2":
            title = input("Enter the title of the book to borrow: ")
            book = library.find_book(title)
            if book:
                print(book.borrow())  # POLYMORPHISM: each book behaves differently
            else:
                print("Book not found.")

        elif choice == "3":
            title = input("Enter the title of the book to return: ")
            book = library.find_book(title)
            if book:
                print(book.return_book())
            else:
                print("Book not found.")

        elif choice == "4":
            title = input("Enter the title of the book to rate: ")
            book = library.find_book(title)
            if book:
                try:
                    rating = int(input("Enter a rating from 0 to 5: "))
                    book.set_rating(rating)
                    print(f"Thanks! Current rating: {book.get_rating()}/5")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                print("Book not found.")

        elif choice == "5":
            print("Exiting Smart Library. See you again! Bye Bye")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
