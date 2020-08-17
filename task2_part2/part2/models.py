from django.db import models
from django.contrib.auth.models import User

class Extend_user(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='user')
	phone_no = models.IntegerField()

	def __str__(self):
		return self.user.username

