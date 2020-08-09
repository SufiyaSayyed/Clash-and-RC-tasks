from django.db import models

class Info(models.Model):
	first_name = models.CharField(max_length=50, unique=True)
	last_name = models.CharField(max_length=50, unique=True)
	email = models.EmailField()
	phone_num = models.IntegerField()
	gender = models.CharField(max_length=10, unique=True)
