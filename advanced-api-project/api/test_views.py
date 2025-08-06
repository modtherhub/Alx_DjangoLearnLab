from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Author, Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.author = Author.objects.create(name="John Doe")
        self.book = Book.objects.create(title="Sample Book", author=self.author, publication_year=2020)
        self.client = APIClient()

        self.client.login(username="testuser", password="testpass")

        self.token_url = reverse('api-token-auth')
        response = self.client.post(self.token_url, {
            'username': 'testuser',
            'password': 'testpass'
        }, format='json')
        self.token = response.data.get('token')
        self.auth_header = {'HTTP_AUTHORIZATION': f'Token {self.token}'}

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_book(self):
        url = reverse('book_all-list')  # viewset route
        data = {
            'title': 'New Book',
            'author': self.author.id,
            'publication_year': 2022
        }
        response = self.client.post(url, data, format='json', **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Book')

    def test_update_book(self):
        url = reverse('book_all-detail', args=[self.book.id])
        data = {
            'title': 'Updated Book Title',
            'author': self.author.id,
            'publication_year': 2021
        }
        response = self.client.put(url, data, format='json', **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Book Title')

    def test_delete_book(self):
        url = reverse('book_all-detail', args=[self.book.id])
        response = self.client.delete(url, **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_book_without_auth(self):
        url = reverse('book_all-list')
        data = {
            'title': 'Unauthorized Book',
            'author': self.author.id,
            'publication_year': 2023
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

