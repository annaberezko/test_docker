from django.contrib.postgres.expressions import ArraySubquery
from django.db.models import OuterRef, Sum, F
from rest_framework import generics

from testapp.models import Book, Employee, Country, City, Order
from testapp.serializers import BookSerializer, EmployeeSerializer, CountrySerializer, TotalRevenuesSerializer


class BooksListView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        """
        Write a single query to retrieve all books that were published in the year 2022 and
        authored by an author whose email ends with "@gmail.com"
        """
        return Book.objects.select_related('author').filter(
            published_date__year=2022,
            author__email__endswith="@gmail.com"
        )


class EmployeesListView(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        """
        Write a single query to retrieve the names of all employees who earn a salary greater than
        or equal to $100,000 and whose manager manages a team of size greater than or equal to 5
        """
        return Employee.objects.filter(
            salary__gte=100000,
            managers__team_size__gte=5
        )


class TotalRevenuesListView(generics.ListAPIView):
    serializer_class = TotalRevenuesSerializer

    def get_queryset(self):
        """
        Write a single query to retrieve the total revenue earned from orders placed by customers
        whose email domain is "gmail.com"
        """
        return Order.objects.select_related('customer').filter(customer__email__endswith="gmail.com").\
            annotate(total_revenue=Sum(F('order_item__unit_price') * F('order_item__quantity'))).order_by('id')


class CountriesListView(generics.ListAPIView):
    serializer_class = CountrySerializer

    def get_queryset(self):
        """
        Write a single query to retrieve all countries, with their cities prefetched and sorted in
        descending order by population
        """
        cities_list = City.objects.filter(country=OuterRef('pk')).order_by('-population').values('name')
        return Country.objects.annotate(cities_list=ArraySubquery(cities_list))
