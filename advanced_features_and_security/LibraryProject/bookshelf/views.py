from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
# Create your views here.
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book_view(request):
    # Only editors/admins can access
    ...
