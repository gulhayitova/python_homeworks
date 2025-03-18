class Book:
    def __init__(self, title, author, is_borrowed = False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
    def to_list(self):
        return [self.title, self.author, self.is_borrowed]
    def from_list(self, booklist):
        self.title = booklist[0]
        self.author = booklist[1]
        self.is_borrowed = booklist[2]

class Member:
    def __init__(self, name, borrowed):
        self.name = name
        self.borrowed = borrowed
    
class Library:
    def __init__(self, books, members):
        self.books = books if books else []
        self.members = members if members else []

    def add_book(self, b_title, b_author):
        book = Book(b_title, b_author)
        self.books.append(book)

    def add_member(self, name):
        member = Member(name, 0)
        self.members.append(member)

    def find_book(self, seek_title, seek_author):
        for book in self.books:
            if book.title == seek_title and book.author == seek_author:
                return book
        return None
    
    def find_member(self, name):
        for member in self.members:
            if member.name == name:
                return member
        return None

# BookNotFoundException: Raised when trying to borrow a book that doesn’t exist in the library.
# BookAlreadyBorrowedException: Raised when a book is already borrowed.
# MemberLimitExceededException: Raised when a member tries to borrow more books than allowed.

    def borrow(self, borrower, title, author):
        book = self.find_book(title, author)
        member = self.find_member(borrower)
        if not book:
            raise BookNotFoundException("The book you are searching for is not found in the library.")
        if book.is_borrowed == True:
            raise BookAlreadyBorrowedException(title)
        if member.borrowed >= 3:
            raise MemberLimitExceededException(borrower)
        book.is_borrowed = True
        member.borrowed = member.borrowed + 1
        return f"'{book.title.capitalize()}' by {book.author.upper()} is borrowed under the name of {borrower.upper()}."

    def return_book(self, borrower, title, author):
        book = self.find_book(title, author)
        member = self.find_member(borrower)
        book.is_borrowed = False
        member.borrowed = member.borrowed - 1


class BookNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)
class BookAlreadyBorrowedException(Exception):
    def __init__(self, book):
        super().__init__(f"'{book.capitalize()}' is already borrowed.")
class MemberLimitExceededException(Exception):
    def __init__(self, member):
        super().__init__(f"{member.upper()}, the number of books you borrowed has reacher the limit!")

books = []
members = []
my_library = Library(books, members)
my_library.add_book("pride and prejudice", "jane austen")
my_library.add_book("emily", "jane austen")
my_library.add_member("john")
my_library.add_member("anna")

print(my_library.borrow('john', 'pride and prejudice', "jane austen"))
print(my_library.find_book("pride and prejudice", "jane austen").is_borrowed)
my_library.return_book('john', 'pride and prejudice', "jane austen")

print(my_library.borrow('anna', 'pride and prejudice', "jane austen"))