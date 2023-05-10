from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse

from testapp.models import Author, Book, Employee, Manager, Customer, Country, City, Order, OrderItem

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
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)


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
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)


class TotalRevenueListViewTests(TestCase):
    def setUp(self):
        customer1 = Customer.objects.create(name='Test Name', email='user1@user.com')
        customer2 = Customer.objects.create(name='Test Name', email='user2@gmail.com')
        customer3 = Customer.objects.create(name='Test Name', email='user3@gmail.com')

        order1 = Order.objects.create(customer=customer1, date_ordered='2023-01-01')
        order2 = Order.objects.create(customer=customer1, date_ordered='2023-01-01')
        order3 = Order.objects.create(customer=customer2, date_ordered='2023-01-01')
        order4 = Order.objects.create(customer=customer2, date_ordered='2023-01-01')
        order5 = Order.objects.create(customer=customer3, date_ordered='2023-01-01')

        OrderItem.objects.create(order=order1, product_name='Test Name', quantity=1, unit_price=5.5)
        OrderItem.objects.create(order=order1, product_name='Test Name', quantity=3, unit_price=25.5)
        OrderItem.objects.create(order=order2, product_name='Test Name', quantity=2, unit_price=15.5)
        OrderItem.objects.create(order=order3, product_name='Test Name', quantity=10, unit_price=10)
        OrderItem.objects.create(order=order3, product_name='Test Name', quantity=8, unit_price=5.5)
        OrderItem.objects.create(order=order4, product_name='Test Name', quantity=10, unit_price=50.5)
        OrderItem.objects.create(order=order5, product_name='Test Name', quantity=8, unit_price=100.5)
        OrderItem.objects.create(order=order5, product_name='Test Name', quantity=19, unit_price=1.7)

    def test_total_revenue(self):
        response = self.client.get(reverse('revenues-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['total_revenue'], 144)
        self.assertEqual(response.data[1]['total_revenue'], 505)
        self.assertEqual(response.data[2]['total_revenue'], 836)


class CountriesListView(TestCase):
    def setUp(self):
        self.country1 = Country.objects.create(name="Ukraine")
        self.country2 = Country.objects.create(name="Poland")

        City.objects.create(name="Dnipro", population=5, country=self.country1)
        City.objects.create(name="Wroclaw", population=8, country=self.country1)
        City.objects.create(name="Odessa", population=7, country=self.country1)

        City.objects.create(name="Warsaw", population=7, country=self.country2)
        City.objects.create(name="Krakow", population=6, country=self.country2)
        City.objects.create(name="Kyiv", population=6, country=self.country2)

    def test_countries_list(self):
        response = self.client.get(reverse('countries-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['cities_list'][0], 'Kyiv')
        self.assertEqual(response.data[0]['cities_list'][1], 'Odessa')
        self.assertEqual(response.data[0]['cities_list'][2], 'Dnipro')
        self.assertEqual(len(response.data), 2)
