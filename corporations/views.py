from .models import Company, Employee
from .serializers import CompanySerializer, EmployeeSerializer
from rest_framework import viewsets, filters


class CompanyViewset(viewsets.ModelViewSet):
	queryset = Company.objects.all()
	serializer_class = CompanySerializer
