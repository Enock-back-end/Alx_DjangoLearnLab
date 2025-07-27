from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Show these fields in the list view
    search_fields = ('title', 'author')  # Search by title or author
    list_filter = ('publication_year',)  # Add a filter by year

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

