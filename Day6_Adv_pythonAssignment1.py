class Library:
    total_books = 0
    all_books = []

    def __init__(self, name):
        self.name, self.borrowed_books = name, []

    def borrow_book(self, book):
        if book in Library.all_books:
            Library.all_books.remove(book)
            self.borrowed_books.append(book)
            Library.total_books -= 1
            print(f"{self.name} borrowed '{book}'.")
        else:
            print(f"'{book}' not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            Library.all_books.append(book)
            Library.total_books += 1
            print(f"{self.name} returned '{book}'.")

    @classmethod
    def view_books(cls):
        print(f"Total books: {cls.total_books} | Available: {cls.all_books}")

# Initialize library
Library.all_books, Library.total_books = ["Python", "AI", "ML"], 3

# Test case
user = Library("John")
Library.view_books()
user.borrow_book("Python")
user.return_book("Python")
Library.view_books()

''' output
Total books: 3 | Available: ['Python', 'AI', 'ML']
John borrowed 'Python'.
John returned 'Python'.
Total books: 3 | Available: ['AI', 'ML', 'Python']
'''
