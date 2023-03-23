from django.views.generic import ListView

from testapp.models import Book


class BooksListView(ListView):
    model = Book
    template_name = 'books.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.all()
