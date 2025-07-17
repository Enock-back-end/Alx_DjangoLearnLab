from relationship_app.models import Author, Book, Library, Librarian
from .models import Book

def books_by_author(author_name):
    return Book.objects.filter(author=author_name)

author = Author.objects.get(name="J.K. Rowling")
books_by_author = Book.objects.filter(author=author)

library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()

librarian = Librarian.objects.get(library=library)
