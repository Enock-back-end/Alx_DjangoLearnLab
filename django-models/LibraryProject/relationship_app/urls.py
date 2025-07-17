from django.urls import path
from .views import list_books_view, LibraryDetailView
from . import views
from .views import LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView

from django.urls import path
from .views.admin_view import admin_view
from .views.librarian_view import librarian_view
from .views.member_view import member_view


from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views.admin_view import admin_view
from .views.librarian_view import librarian_view
from .views.member_view import member_view



urlpatterns = [
    path('books/', list_books_view, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    


    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),


    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),


     path('books/', views.list_books, name='list_books'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),

    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),

    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
    

    
]
