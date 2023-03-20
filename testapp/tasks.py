from test_docker.celery import app
from testapp.models import Book


@app.task
def add(x, y):
    print("Hello, celery")
    # Book.objects.create(name="Celery book")
    return x + y


@app.task
def print_text():
    print("One minute later...")
