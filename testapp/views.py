from rest_framework import generics

from testapp.models import Book, Employee
from testapp.serializers import BookSerializer, EmployeeSerializer


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
