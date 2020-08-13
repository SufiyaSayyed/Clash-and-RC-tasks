#from django.db import models
#from django.contrib.auth.models import User
#from django.db.models.signals import post_save
#from django.dispatch import receiver

#class Extend_user(models.Model):
#	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#	phone_no = models.IntegerField()

#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
#	if created:
#		Extended_user.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, **kwargs):
#	instance.profile.save()