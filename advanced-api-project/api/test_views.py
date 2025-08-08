from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book
from .serializers import BookSerializer


class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.client = APIClient()

        # Create two books
        self.book1 = Book.objects.create(
            title="Django for APIs", author=self.user, publication_year=2021
        )
        self.book2 = Book.objects.create(
            title="Python Clean Code", author=self.user, publication_year=2020
        )

        # Endpoints
        self.list_url = reverse('book-list')  # Ensure URL name matches urls.py
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book1.id})
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', kwargs={'pk': self.book1.id})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book1.id})

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book_unauthenticated(self):
        response = self.client.post(self.create_url, {
            "title": "New Book",
            "author": self.user.id,
            "publication_year": 2023
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.create_url, {
            "title": "New Book",
            "author": self.user.id,
            "publication_year": 2023
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "New Book")

    def test_update_book(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.put(self.update_url, {
            "title": "Updated Title",
            "author": self.user.id,
            "publication_year": 2022
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated Title")

    def test_delete_book(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    def test_filter_books_by_title(self):
        response = self.client.get(self.list_url, {'title': 'Django for APIs'})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Django for APIs')

    def test_search_books(self):
        response = self.client.get(self.list_url, {'search': 'Clean'})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Python Clean Code')

    def test_ordering_books_by_year(self):
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.data[0]['publication_year'], 2020)
        self.assertEqual(response.data[1]['publication_year'], 2021)

    def test_login_and_create_book(self):
        logged_in = self.client.login(username="testuser", password="testpass123")
        self.assertTrue(logged_in)  # Ensure login succeeded

        response = self.client.post(self.create_url, {
            "title": "Login Book",
            "author": self.user.id,
            "publication_year": 2024
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "Login Book")
