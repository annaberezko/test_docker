from django.urls import path

from testapp.views import BooksListView, EmployeesListView

urlpatterns = [
    path('/books-list/', BooksListView.as_view(), name='books-list'),
    path('/employees-list/', EmployeesListView.as_view(), name='employees-list'),
]
