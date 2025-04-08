from digitalbook import DigitalBook

ebook = DigitalBook("Python for All", "Guido van Rossum", 2020, 75)

print(ebook.get_details())
print(ebook.stream())          # Unique to digital books
print(ebook.borrow())          # Overrides the original method
