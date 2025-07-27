from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
# Create your views here.
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book_view(request):
    # Only editors/admins can access
    ...
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book

@login_required
@permission_required('bookshelf.view_book', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})
