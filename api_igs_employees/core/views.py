from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response

from .filters import filter_queryparams
from .serializers import DepartamentSerializer, EmployeeSerializer
from .models import Departament, Employee
# Create your views here.

class DepartamentList(generics.ListCreateAPIView):
    model = Departament
    serializer_class = DepartamentSerializer

    def get_queryset(self):
        queryset = Departament.objects.all()
        if 'name' in self.request.query_params:
            queryset = queryset.filter(name__icontains=self.request.query_params.get('name'))

        return queryset

    def list(self, request):

        serializer = DepartamentSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('name')
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        employees = filter_queryparams(self.request, self.queryset)

        return employees

