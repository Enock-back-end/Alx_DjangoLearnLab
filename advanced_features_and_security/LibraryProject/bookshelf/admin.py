from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Show these fields in the list view
    search_fields = ('title', 'author')  # Search by title or author
    list_filter = ('publication_year',)  # Add a filter by year
