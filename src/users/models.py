from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.
#===================================================================================

class User(AbstractUser):
	"""User Abstract Class Create """
	is_student = models.BooleanField(default=False)
	is_instructor = models.BooleanField(default=False)
	
	is_email_verified = models.BooleanField(default=False)
	activation_key = models.CharField(max_length=255, blank=True, null=True)
	key_expiry_time = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.username

