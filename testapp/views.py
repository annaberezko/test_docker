from django.views.generic import ListView

from testapp.models import Book
# from testapp.tasks import add


class BooksListView(ListView):
    model = Book
    template_name = 'books.html'
    context_object_name = 'books'

    # def get_queryset(self):
    #     print("Hello, queryset")
    #     temp = add.delay(1, 2)
    #     print(temp)
    #     return Book.objects.all()
