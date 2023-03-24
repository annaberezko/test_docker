from rest_framework import serializers

from testapp.models import Book, Employee


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', )


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('name', )
