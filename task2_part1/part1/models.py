from django.db import models

class Info(models.Model):
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	email = models.EmailField()
	phone_no = models.IntegerField()
	gender = models.CharField(max_length = 50)
	