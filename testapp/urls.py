from django.urls import path

from testapp.views import BooksListView, EmployeesListView, TotalRevenuesListView, CountriesListView

urlpatterns = [
    path('books-list/', BooksListView.as_view(), name='books-list'),
    path('employees-list/', EmployeesListView.as_view(), name='employees-list'),
    path('revenues-list/', TotalRevenuesListView.as_view(), name='revenues-list'),
    path('countries-list/', CountriesListView.as_view(), name='countries-list'),
]
