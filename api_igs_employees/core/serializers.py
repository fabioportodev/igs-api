from rest_framework import serializers

from .models import Employee, Departament

class DepartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departament
        fields = ('id', 'name')

class EmployeeSerializer(serializers.ModelSerializer):
    departament = DepartamentSerializer()
    class Meta:
        model = Employee
        fields = ('id', 'name', 'email', 'departament')