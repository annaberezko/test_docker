from rest_framework import serializers

from testapp.models import Book, Employee, Country, Order


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', )


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('name', )


class TotalRevenuesSerializer(serializers.ModelSerializer):
    total_revenue = serializers.IntegerField()

    class Meta:
        model = Order
        fields = ('id', 'date_ordered', 'total_revenue')


class CountrySerializer(serializers.ModelSerializer):
    cities_list = serializers.ListField()

    class Meta:
        model = Country
        fields = ('name', 'cities_list', )
