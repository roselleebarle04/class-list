from django.db import models

class Student(models.Model):
	id_number = models.CharField(max_length=200)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	is_active = models.BooleanField(default=True)
