class Book:
    def __init__(self, title, author, year):
        """
        Constructor method to initialize the book object
        """
        self.title = title
        self.author = author
        self.year = year
        self.available = True  #Default to available
        self.__rating = 0 

    def borrow(self):
        """
        Marks the book as borrowed if the book is available
        """
        if self.available:
            self.available = False
            return f"You have borrowed '{self.title}'."
        return f"'{self.title}' is currently NOT available."
    
    def return_book(self):
        """
        Marks the Book as returned
        """
        self.available = True
        return f"'{self.title}' has been returned."
    
    def get_details(self):
        """
        Returns formatted book information.
        """
        return f"{self.title} by {self.author} {self.year}"
    
    def set_rating(self, rating):
        """
        Set a rating from 0 to 5 for the book.
        This is an example of encapsulation: rating is private
        """
        if 0 <= rating <= 5:
            self.__rating = rating
        else:
            print("Rating must be between 0 and 5")

    def get_rating(self):
        """
        Get the current ratings of the book
        """
        return self.__rating
    

    # Book.get_details()
    # Book.available =
    
        
    