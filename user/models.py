from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
	is_visitor = models.BooleanField(default=False)
	is_recepcionist = models.BooleanField(default=False)
	is_funsionariu = models.BooleanField(default=False)