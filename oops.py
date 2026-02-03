class oops:

    def __init__(self):
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)
        print(book_name, "added to library.")

    def remove_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(book_name, "removed from library.")
        else:
            print("Book not found!")

    def display_books(self):
        print("\nBooks Available in Library:")
        for book in self.books:
            print("-", book)


lib = Library()
lib.add_book("Python Programming")
lib.add_book("Java Basics")
lib.display_books()
lib.remove_book("Java Basics")
lib.display_books()
