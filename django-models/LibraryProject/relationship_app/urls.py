from django.urls import path
from .views import list_books_view, LibraryDetailView
from . import views
from .views import LibraryDetailView


urlpatterns = [
    path('books/', list_books_view, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
        path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
        path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),

    
]
