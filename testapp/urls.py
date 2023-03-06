from django.urls import path

from testapp.views import BooksListView

urlpatterns = [
    path('', BooksListView.as_view(), name='books-list'),
    ]
