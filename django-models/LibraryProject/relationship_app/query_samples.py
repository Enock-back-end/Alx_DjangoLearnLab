from .models import Library, Book


def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.book_set.all()

def books_by_author(author_name):
    return Book.objects.filter(author=author_name)


def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian
