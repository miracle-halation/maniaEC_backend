from django.contrib import admin
from corporations.models import Company, Employee

# Register your models here.
admin.site.register(Company)
admin.site.register(Employee)