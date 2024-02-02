from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import UserModel, BookModel, BookDetailsModel, BorrowedBooksModel
from .serializers import UserSerializer, BookSerializer, BookDetailsSerializer, BorrowedBooksSerializer

class UserViewTests(APITestCase):
    def test_get_all_users(self):
        url = reverse('users')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        url = reverse('users')
        data = {'name': 'John Doe', 'email': 'john@example.com', 'membership_date': '2022-01-01'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_by_id(self):
        user = UserModel.objects.create(name='Test User', email='test@example.com', membership_date='2022-01-01')
        url = reverse('user_detail', args=[user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class BookViewTests(APITestCase):
    def test_get_all_books(self):
        url = reverse('books')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book(self):
        url = reverse('books')
        data = {'title': 'Test Book', 'isbn': '1234567890', 'published_date': '2022-01-01', 'genre': 'Fiction'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book(self):
        book = BookModel.objects.create(title='Test Book', isbn='1234567890', published_date='2022-01-01', genre='Fiction')
        url = reverse('books')
        data = {'title': 'Updated Test Book'}
        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class BorrowedBooksViewTests(APITestCase):

    def test_return_book(self):
        user = UserModel.objects.create(name='Test User', email='test@example.com', membership_date='2022-01-01')
        book = BookModel.objects.create(title='Test Book', isbn='1234567890', published_date='2022-01-01', genre='Fiction')
        borrowed_book = BorrowedBooksModel.objects.create(userid=user, bookid=book, borrowed_date='2022-02-01', return_date='2022-02-15')

        url = reverse('borrowed_book')
        data = {'return_date': '2022-02-15'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Additional test case...........
        updated_response = self.client.get(reverse('borrowed_book'))
        self.assertNotIn(book.id, [item['book'] for item in updated_response.data['borrowed_books']])


