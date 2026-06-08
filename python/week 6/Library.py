class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            print(f"Sorry, '{self.title}' is already borrowed")
        else:
            self.is_borrowed = True
            print(f"You borrowed '{self.title}'")

    def return_book(self):
        if not self.is_borrowed:
            print(f"'{self.title}' was not borrowed")
        else:
            self.is_borrowed = False
            print(f"You returned '{self.title}'")

    def show(self):
        if self.is_borrowed:
            status = "Borrowed"
        else:
            status = "Available"

        print(f"{self.title} by {self.author} ({self.year}) - {status}")


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' to {self.name}")

    def show_all(self):
        print(f"\n=== {self.name} ===")
        for book in self.books:
            book.show()

    def count_available(self):
        count = 0
        for book in self.books:
            if not book.is_borrowed:
                count += 1
        return count

lib = Library("Tuwaiq Library")
b1 = Book("Clean Code", "Robert Martin", 2008)
b2 = Book("Python Crash Course", "Eric Matthes", 2019)
b3 = Book("The Pragmatic Programmer", "Andy Hunt", 1999)
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)
lib.show_all()
b1.borrow()
b1.borrow()
b1.return_book()
print("Available books:", lib.count_available())
lib.show_all()