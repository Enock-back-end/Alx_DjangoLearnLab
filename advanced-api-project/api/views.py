from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# ListView for retrieving all books (GET)
class BookListView(generics.ListAPIView):
    """
    GET: Return a list of all books.
    Publicly accessible without authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# DetailView for retrieving a single book by ID (GET)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Public read access

# CreateView for adding a new book (POST)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Auth required

# UpdateView for modifying an existing book (PUT, PATCH)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Auth required

# DeleteView for removing a book (DELETE)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Auth required


