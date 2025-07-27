```python
# Django shell:
# python manage.py shell

from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# retrieving all books
books = Book.objects.all()
print(books)

# Expected Output:
# <QuerySet []> — confirms the book was deleted
