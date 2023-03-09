from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse

from testapp.models import Author, Book

User = get_user_model()


class BooksListViewTests(TestCase):
    def setUp(self):
        author = Author.objects.create(name='Test Name')
        Book.objects.create(name="Test book 1", author=author)
        Book.objects.create(name="Test book 2", author=author)

    def test_books_list(self):
        response = self.client.get(reverse('books-list'))
        self.assertEqual(response.status_code, 200)
