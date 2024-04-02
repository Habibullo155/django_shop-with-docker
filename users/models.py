from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'users'

        def __str__(self):
            return self.username
