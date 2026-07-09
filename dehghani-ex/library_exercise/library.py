class Printable:
    def __str__(self):
        return f"""{self.__class__.__name__} : {self.__dict__}"""

    def __repr__(self):
        return f"{self.__class__.__name__}:({self.__dict__})"

class Book(Printable):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        return self.title == other.title

    def __hash__(self):
        return hash(self.title)

class Library(Printable):

    def __init__(self):
        self.books = set()

    def add_book(self, title: str, author: str):
        book = Book(title, author)
        self.books.add(book)
        print(f"added book {book} to library")
        return book

    def remove_book(self, title: str):
        deleting_book = None
        i = 0
        for book in self.books:
            i+=1
            if book.title == title:
                deleting_book = book
                print(f"removed book {book} from library on iteration {i} on total {len(self.books)}")
                break
        if deleting_book is not None:
            self.books.remove(deleting_book)
        else:
            print(f"book {title} is not in library")

    def search_book(self, title: str):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def show_books(self):
        print(self.books)