import email
from django.db import models

# Create your models here.
class Company(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
			return self.name

class Employee(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField(max_length=255, unique=True)
	password = models.CharField(max_length=255)
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	manager = models.BooleanField()

	def __str__(self):
		return self.name