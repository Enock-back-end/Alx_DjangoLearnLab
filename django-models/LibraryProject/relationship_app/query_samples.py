from .models import Library, Author, Book, Librarian

def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)
