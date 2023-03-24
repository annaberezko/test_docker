from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()


class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    salary = models.IntegerField()


class Manager(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='managers')
    team_size = models.IntegerField()


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_ordered = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)


class Country(models.Model):
    name = models.CharField(max_length=100)


class City(models.Model):
    name = models.CharField(max_length=100)
    population = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
