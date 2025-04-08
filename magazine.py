from book import Book

class Magazine(Book):
    def __init__(self, title, editor, year):
        # We still call the parent constructor, but use 'editor' instead of 'author'
        super().__init__(title, editor, year)


    def borrow(self):
        """
        Magazine can't be borrowed - Override borrow method
        """
        return f"{self.title} is a Magazine and cannot be borrowed."
