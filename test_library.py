from book import Book
from library import Library

lib = Library("Test Library")
lib.add_book(Book("Atomic Habits", "James Clear", 2018))
lib.add_book(Book("Deep Work", "Cal Newport", 2016))

# print("Library Catalog:")
# for book in lib.list_books():
#     print("\n", book)

found = lib.find_book("Deep WORK")
print(found.borrow()) if found else print("Book not Found")
