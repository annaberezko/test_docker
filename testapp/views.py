from django.views.generic import ListView

from testapp.models import Book

class BooksListView(ListView):
    model = Book
    template_name = 'books.html'
    context_object_name = 'books'
