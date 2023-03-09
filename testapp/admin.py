from django.contrib import admin

from testapp.models import Book, Author

admin.site.register(Author)
admin.site.register(Book)
