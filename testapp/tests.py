from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse

from testapp.models import Author, Book, Employee, Manager

User = get_user_model()


class BooksListViewTests(TestCase):
    def setUp(self):
        author1 = Author.objects.create(name='Test Name', email='user1@user.com')
        author2 = Author.objects.create(name='Test Name', email='user2@gmail.com')

        Book.objects.create(name="Test book 1", author=author1, published_date='2022-01-02')
        Book.objects.create(name="Test book 2", author=author2, published_date='2022-01-02')
        Book.objects.create(name="Test book 2", author=author2, published_date='2021-01-02')

    def test_books_list(self):
        response = self.client.get(reverse('books-list'))
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, 200)


class EmployeesListViewTests(TestCase):
    def setUp(self):
        employee1 = Employee.objects.create(name='Test Name', department='Department name', salary=20000)
        employee2 = Employee.objects.create(name='Test Name', department='Department name', salary=100000)
        employee3 = Employee.objects.create(name='Test Name', department='Department name', salary=120000)
        employee4 = Employee.objects.create(name='Test Name', department='Department name', salary=200000) # noqa

        Manager.objects.create(employee=employee1, team_size=6)
        Manager.objects.create(employee=employee2, team_size=0)
        Manager.objects.create(employee=employee3, team_size=5)

    def test_employees_list(self):
        response = self.client.get(reverse('employees-list'))
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, 200)
