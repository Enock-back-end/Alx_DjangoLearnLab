from .models import Library, Author, Book, Librarian
from .models import Author, Book
from .models import Librarian, Library
books = Book.objects.all()
print(books)

author_name = input() 
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(books_by_author)



# all books in a library
def list_books_in_library(library_id):
    return Book.objects.filter(library_id=library_id)

# all books by a specific author
def books_by_author(author_name):
    return Book.objects.filter(author__name=author_name)

# Retrieving the librarian for a library
def get_librarian_by_library(library_id):
    return Librarian.objects.get(library_id=library_id)

library = Library.objects.get(name="Central Library") 
librarian = Librarian.objects.get(library=library)
print(librarian)

def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)
